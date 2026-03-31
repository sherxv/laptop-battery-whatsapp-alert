# ── Your WhatsApp Number ───────────────────────────────────────────────────────
PHONE_NUMBER = "+91XXXXXXXXXX"          # e.g. "+919876543210"
 
# ── Battery Settings ───────────────────────────────────────────────────────────
BATTERY_THRESHOLD      = 30            # Alert when battery is AT or BELOW this %
CHECK_INTERVAL_MIN     = 10            # Check battery every N minutes
 
# ── Google Meet Schedule ───────────────────────────────────────────────────────
# Format: "YYYY-MM-DD HH:MM"  (24-hour clock)
MEET_SCHEDULE = [
    "2026-04-01 10:00"
    # "2026-04-02 09:00",
]
 
REMINDER_MINUTES_BEFORE = 5            # Send reminder this many minutes before meet
 
# ── pywhatkit Settings ─────────────────────────────────────────────────────────
WAIT_TIME  = 25               # Seconds to wait for WhatsApp Web to load
TAB_CLOSE  = True                      # Close browser tab after sending
CLOSE_TIME = 5                         # Seconds before closing the tab
