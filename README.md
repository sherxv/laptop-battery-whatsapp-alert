

# 🔋 Laptop Battery & Meet Reminder WhatsApp Alert

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A Python-based productivity assistant that monitors your laptop battery and sends instant WhatsApp alerts plus Google Meet reminders, so you never miss a meeting or lose power during deadlines.**

</div>

---

## 📸 Preview

```
2026-03-31 12:38:55  [INFO]  🚀 Personal Productivity Assistant started.
2026-03-31 12:38:55  [INFO]     Battery threshold    : 30%
2026-03-31 12:38:55  [INFO]     Battery check every  : 10 min
2026-03-31 12:38:55  [INFO]     Meet reminder buffer : 5 mins before
2026-03-31 12:38:55  [INFO]  Battery: 57.0%  |  Charging ⚡
2026-03-31 12:38:55  [INFO]  ✅ Running... Press Ctrl+C to stop.
```

---

## Features

| Feature | Description |
|---|---|
| 🔋 Battery Monitoring | Checks battery every 10 minutes automatically |
| 📲 WhatsApp Alerts | Sends free WhatsApp message when battery drops below 30% |
| 🔔 Meet Reminders | WhatsApp + desktop notification 5 mins before Google Meet |
| 🔕 Smart Alerting | Re-alerts only if battery drops another 3% — no spam |
| 🔄 Auto Reset | Alert resets automatically when charger is plugged in |
| 📋 Activity Logging | All events saved to `assistant.log` for review |
| 💸 100% Free | Uses WhatsApp Web — no API keys, no subscriptions |

---

## Project Structure

```
laptop-battery-whatsapp-alert/
│
├── main.py                 # Core script — run this to start
├── config.py               # Your private settings (gitignored)
├── config.example.py       # Setup template — copy this to config.py
├── requirements.txt        # Python dependencies
├── .gitignore              # Keeps your private data off GitHub
├── assistant.log           # Auto-generated activity log
└── README.md               # You are here
```

---

## Setup & Installation

### Prerequisites
- Python 3.10 or higher
- WhatsApp account
- Google Chrome / Firefox / Edge browser

### 1. Clone the repository

```bash
git clone https://github.com/sherxv/laptop-battery-whatsapp-alert.git
cd laptop-battery-whatsapp-alert
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your settings

```bash
cp config.example.py config.py
```

Open `config.py` and fill in your details:

```python
PHONE_NUMBER = "+919876543210"    # Your WhatsApp number with country code

MEET_SCHEDULE = [
    "2026-04-02 10:00",           # Add your meeting times here
    "2026-04-02 15:30",           # Format: "YYYY-MM-DD HH:MM"
]
```

### 4. Log in to WhatsApp Web

Open [web.whatsapp.com](https://web.whatsapp.com) in your browser and log in. Keep the tab open while the script runs.

### 5. Run the assistant

```bash
python main.py
```

---

## Configuration Options

Open `config.py` to customize these settings:

| Setting | Default | Description |
|---|---|---|
| `PHONE_NUMBER` | — | Your WhatsApp number with country code |
| `BATTERY_THRESHOLD` | `30` | Send alert when battery is at or below this % |
| `CHECK_INTERVAL_MIN` | `10` | How often to check battery (in minutes) |
| `MEET_SCHEDULE` | `[]` | List of meeting times in `"YYYY-MM-DD HH:MM"` format |
| `REMINDER_MINUTES_BEFORE` | `5` | How many minutes before meet to send reminder |
| `WAIT_TIME` | `20` | Seconds for WhatsApp Web to load before sending |

---

## Sample WhatsApp Messages

**Battery Alert:**
```
🪫 Battery Alert!

Battery is at 28% — not plugged in.
Please connect your charger now! 🔌⚡

Sent at 03:45 PM
```

**Google Meet Reminder:**
```
🔔 Google Meet Reminder!

Your meeting starts in 5 minutes!
📅 Scheduled: 2026-04-01 15:30
⏰ Current time: 03:25 PM

Get ready to join! 💻
```

---

## Tech Stack

| Library | Purpose |
|---|---|
| [psutil](https://pypi.org/project/psutil/) | Reading real-time battery status |
| [pywhatkit](https://pypi.org/project/pywhatkit/) | Sending WhatsApp messages via WhatsApp Web |
| [pyautogui](https://pypi.org/project/pyautogui/) | Force-pressing Enter to send messages |
| [schedule](https://pypi.org/project/schedule/) | Running periodic background checks |
| [plyer](https://pypi.org/project/plyer/) | Desktop popup notifications |

---

## Run in Background

Keep the assistant running silently without a terminal window:

**Windows:**
```bash
pythonw main.py
```

**macOS / Linux:**
```bash
nohup python main.py &
```

---

## Security

- `config.py` is listed in `.gitignore` and **never uploaded to GitHub**
- Your phone number stays private on your local machine only
- Use `config.example.py` as a safe template when sharing or cloning

---

##  Common Issues

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | Run `python -m pip install -r requirements.txt` |
| Message goes to draft | Increase `WAIT_TIME` to `25` in `config.py` |
| `UnicodeEncodeError` | Add `sys.stdout.reconfigure(encoding="utf-8")` at top of `main.py` |
| Meet reminder not triggering | Make sure meet time is in the future and script is running |

---

## Contributing

Pull requests are welcome! If you have ideas for new features, Telegram support, email alerts, calendar sync, auto-startup - feel free to open an issue.

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "added your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

<div align="center">

Built with 🐍 Python &nbsp;|&nbsp; Made by [Shruti Priya](https://github.com/sherxv)

*Perfect for students, developers, and anyone who forgets to charge their laptop!* ⚡

</div>
