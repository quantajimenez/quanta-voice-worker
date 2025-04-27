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
        print(f"✅ Full Response: {response.text}")  # Add full response print
    except Exception as e:
        print(f"❌ Clock Message failed: {e}")

def run_clock_alert():
    print("🕒 Clock Loop Started Successfully...")  # 🛑 Add this print

    # 🔍 DEBUG: Confirm env vars are pulled correctly
    print(f"🔍 BOT_TOKEN starts with: {BOT_TOKEN[:10] if BOT_TOKEN else 'None'}")
    print(f"🔍 CHAT_ID is: {CHAT_ID if CHAT_ID else 'None'}")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Missing BOT_TOKEN or CHAT_ID. Exiting clock.")
        return

    while True:
        try:
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")
            send_message(f"🟢 [{timestamp}] Clock Alert: System heartbeat alive!")
            print(f"✅ Clock Tick Sent at {timestamp}")
        except Exception as e:
            print(f"❌ Error inside clock loop: {e}")
        
        time.sleep(10)  # Send heartbeat every 10 seconds
