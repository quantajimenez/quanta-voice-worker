import time
from datetime import datetime
import requests
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        print(f"✅ Clock Message sent | Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Clock Message failed: {e}")

def run_clock_alert():
    print("🕒 Clock test triggered manually...")

    # 🔍 DEBUG: Confirm env vars are pulled correctly
    print(f"🔍 BOT_TOKEN starts with: {BOT_TOKEN[:10] if BOT_TOKEN else 'None'}")
    print(f"🔍 CHAT_ID is: {CHAT_ID if CHAT_ID else 'None'}")

    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    send_message(f"🟢 [{timestamp}] Clock Alert: Manual test successful!")
