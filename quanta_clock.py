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
    print("⏱️ Clock loop running...")
    while True:
        now = datetime.now()
        if now.minute % 15 == 0 and now.second < 5:
            timestamp = now.strftime("%H:%M:%S")
            send_message(f"🕒 [{timestamp}] Clock Alert: New 15-minute candle!")
            time.sleep(10)
        time.sleep(1)
