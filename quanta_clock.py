import time
import os
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("CLOCK_BOT_TOKEN")
CHAT_ID = os.getenv("CLOCK_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        print(f"✅ Clock Message sent | Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Clock Message failed: {e}")

def run_clock_alert():
    print("🕒 Clock loop started...")
    
    while True:
        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        send_message(f"🕰️ Clock Tick: {timestamp}")
        
        time.sleep(10)  # wait 10 seconds before next tick
