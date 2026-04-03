import os
import time
import datetime
import requests

# =============================================================
# TELEGRAM CONFIGURATION
# =============================================================
TOKEN = "YOUR_BOT_TOKEN"   # Replace with your Telegram Bot token
CHAT_ID = "YOUR_CHAT_ID"   # Replace with your Telegram Chat ID

# =============================================================
# MONITORING TARGETS
# =============================================================
TARGETS = {
    "Router":           "192.168.137.1",
    "Internet (Google DNS)": "8.8.8.8",
    "Internet (Cloudflare)": "1.1.1.1",
}

# How often to check (seconds)
CHECK_INTERVAL = 60


def send_telegram_msg(message: str) -> None:
    """Send a message to the configured Telegram chat."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"[ERROR] Failed to send Telegram message: {e}")


def check_ping(host: str) -> bool:
    """Return True if the host responds to a single ICMP ping."""
    response = os.system(f"ping -c 1 -W 2 {host} > /dev/null 2>&1")
    return response == 0


def get_timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =============================================================
# STARTUP NOTIFICATION
# =============================================================
send_telegram_msg(
    f"✅ Network Guard started on Raspberry Pi 1B\n"
    f"Monitoring {len(TARGETS)} target(s): {', '.join(TARGETS.keys())}\n"
    f"Check interval: {CHECK_INTERVAL}s"
)
print(f"[{get_timestamp()}] Network Guard started. Monitoring: {list(TARGETS.keys())}")

# =============================================================
# MAIN MONITORING LOOP
# =============================================================
while True:
    now = get_timestamp()

    for name, ip in TARGETS.items():
        if not check_ping(ip):
            msg = f"🚨 ALARM: {name} ({ip}) is not responding!\n[{now}]"
            print(msg)
            send_telegram_msg(msg)
        else:
            print(f"[{now}] ✅ {name} ({ip}) — OK")

    time.sleep(CHECK_INTERVAL)
