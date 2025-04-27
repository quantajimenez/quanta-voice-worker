from flask import Flask
import threading
import time
from datetime import datetime
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    print(f"🚀 Sending to Telegram: {payload}")  # << DEBUG LINE
    try:
        response = requests.post(url, json=payload)
        print(f"✅ Telegram response: {response.status_code} | {response.text}")  # << DEBUG LINE
    except Exception as e:
        print(f"❌ Telegram send error: {e}")

def clock_loop():
    print("🕒 Clock Loop Started Successfully...")
    print(f"🔍 BOT_TOKEN starts with: {BOT_TOKEN[:10] if BOT_TOKEN else 'None'}")
    print(f"🔍 CHAT_ID is: {CHAT_ID if CHAT_ID else 'None'}")

    while True:
        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        send_message(f"🟢 [{timestamp}] Clock Alert: I'm alive.")
        time.sleep(10)

@app.route("/")
def home():
    return "🕒 Clock Worker is Running!"

if __name__ == "__main__":
    threading.Thread(target=clock_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
