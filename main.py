from flask import Flask
import threading
import time
from datetime import datetime
import requests
import os

app = Flask(__name__)

def send_message(text):
    # Reload env vars every time in case of updates
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Missing BOT_TOKEN or CHAT_ID.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    headers = {"Content-Type": "application/json"}
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        print(f"🚀 Sending to Telegram: {payload}")
        response = requests.post(url, headers=headers, json=payload)
        print(f"🛬 Response: {response.status_code} {response.text}")

        if response.status_code != 200:
            raise Exception(f"Telegram API Error: {response.status_code} - {response.text}")

        print("✅ Message successfully sent!")

    except Exception as e:
        print(f"❌ Failed to send message: {e}")
        raise e  # Crash the thread if Telegram fails badly

def clock_loop():
    print("🕒 Clock Loop Started Successfully...")

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
