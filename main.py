"""
 Personal Productivity Assistant                 
 Battery Monitor + Google Meet Reminders                
 uses WhatsApp Web via pywhatkit     

"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

import time
import logging
import psutil
import schedule
import pyautogui
import pywhatkit as pwk
from plyer import notification
from datetime import datetime
from config import (
    PHONE_NUMBER,
    BATTERY_THRESHOLD,
    CHECK_INTERVAL_MIN,
    MEET_SCHEDULE,
    REMINDER_MINUTES_BEFORE,
    WAIT_TIME,
    TAB_CLOSE,
    CLOSE_TIME,
)

# Logging Setup 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
    logging.FileHandler("assistant.log", encoding="utf-8"),
    logging.StreamHandler(stream=open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)),
    ],
)
log = logging.getLogger(__name__)

# State 
_last_battery_alert: float | None = None
_is_charging: bool = False
_meets_notified: set = set()


#  Helpers 
def send_whatsapp(msg: str, label: str) -> None:
    """Send a WhatsApp message and force-press Enter to actually send it."""
    try:
        pwk.sendwhatmsg_instantly(PHONE_NUMBER, msg, WAIT_TIME, TAB_CLOSE, CLOSE_TIME)
        time.sleep(WAIT_TIME)          # wait for WhatsApp Web to fully load
        pyautogui.press("enter")       # force-press Enter — fixes draft issue
        log.info(f"✅ {label} sent successfully.")
    except Exception as e:
        log.error(f"❌ Failed to send {label}: {e}")


# Battery 
def get_battery_status() -> tuple[float, bool] | tuple[None, None]:
    battery = psutil.sensors_battery()
    if battery is None:
        return None, None
    return battery.percent, battery.power_plugged


def send_battery_alert(percent: float) -> None:
    now_str = datetime.now().strftime("%I:%M %p")
    msg = (
        f"🪫 *Laptop Battery Alert!*\n\n"
        f"Battery is at *{percent:.0f}%* — not plugged in.\n"
        f"Please connect your charger now! 🔌⚡\n\n"
        f"_Sent at {now_str}_"
    )
    log.warning(f"🔴 Battery at {percent:.1f}% — sending alert…")
    send_whatsapp(msg, "Battery alert")


def check_battery() -> None:
    global _last_battery_alert, _is_charging

    percent, plugged = get_battery_status()
    if percent is None:
        log.warning("⚠️  Battery info unavailable.")
        return

    plug_label = "Charging ⚡" if plugged else "On Battery 🔋"
    log.info(f"Battery: {percent:.1f}%  |  {plug_label}")

    # Reset alert state when charger is connected
    if plugged:
        if _last_battery_alert is not None:
            log.info("🟢 Charger connected — alert state reset.")
        _last_battery_alert = None
        _is_charging = True
        return

    _is_charging = False

    # Alert if low AND (never alerted OR battery dropped 3% more since last alert)
    if percent <= BATTERY_THRESHOLD:
        if _last_battery_alert is None or percent <= _last_battery_alert - 3:
            send_battery_alert(percent)
            _last_battery_alert = percent
        else:
            log.info("🔕 Alert already sent. Waiting for 3% more drop or plug-in.")


# Meet Reminders
def send_meet_reminder(meet_time_str: str) -> None:
    now_str = datetime.now().strftime("%I:%M %p")
    msg = (
        f"🔔 *Google Meet Reminder!*\n\n"
        f"Your meeting starts in *{REMINDER_MINUTES_BEFORE} minutes!*\n"
        f"📅 Scheduled: {meet_time_str}\n"
        f"⏰ Current time: {now_str}\n\n"
        f"_Get ready to join!_ 💻"
    )

    log.info(f"📅 Sending meet reminder for {meet_time_str}")

    # Desktop notification
    try:
        notification.notify(
            title="🔔 Google Meet in 5 mins!",
            message=f"Scheduled: {meet_time_str}",
            timeout=10,
        )
    except Exception as e:
        log.warning(f"Desktop notification failed: {e}")

    # WhatsApp message
    send_whatsapp(msg, "Meet reminder")


def check_meet_reminders() -> None:
    now = datetime.now()

    for meet_str in MEET_SCHEDULE:
        try:
            meet_time = datetime.strptime(meet_str, "%Y-%m-%d %H:%M")

            # Skip meets already in the past
            if meet_time < now:
                continue

            time_diff_minutes = (meet_time - now).total_seconds() / 60

            # Trigger within a 30-second window of the reminder time
            if abs(time_diff_minutes - REMINDER_MINUTES_BEFORE) <= 0.5:
                if meet_str not in _meets_notified:
                    send_meet_reminder(meet_str)
                    _meets_notified.add(meet_str)

        except ValueError:
            log.error(f"❌ Invalid meet time format: '{meet_str}' — use 'YYYY-MM-DD HH:MM'")


# Main 
def main() -> None:
    log.info("🚀 Personal Productivity Assistant started.")
    log.info(f"   Battery threshold    : {BATTERY_THRESHOLD}%")
    log.info(f"   Battery check every  : {CHECK_INTERVAL_MIN} min")
    log.info(f"   Meet reminder buffer : {REMINDER_MINUTES_BEFORE} mins before")
    log.info(f"   Meets scheduled      : {len(MEET_SCHEDULE)}")
    log.info(f"   Alerting number      : {PHONE_NUMBER}")

    # Schedule recurring jobs
    schedule.every(CHECK_INTERVAL_MIN).minutes.do(check_battery)
    schedule.every(1).minutes.do(check_meet_reminders)

    # Run immediately on startup
    check_battery()
    check_meet_reminders()

    log.info("✅ Running... Press Ctrl+C to stop.\n")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("👋 Stopped by user.")