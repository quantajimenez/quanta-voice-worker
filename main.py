from flask import Flask
import threading
import time
from datetime import datetime
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def test_token_alive():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Token is alive.")
        else:
            print(f"⚠️ Token might be restricted. Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"❌ Token test failed: {e}")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Telegram API Error: {response.status_code} - {response.text}")
        print(f"✅ Clock Message sent | Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Clock Message failed: {e}")
        time.sleep(30)
        print("🔁 Retrying message...")
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"✅ Retry success.")
            else:
                print(f"❌ Retry failed: {response.status_code} | {response.text}")
        except Exception as e2:
            print(f"❌ Second failure: {e2}")

def clock_loop():
    print("🕒 Clock Loop Started Successfully...")
    print(f"🔍 BOT_TOKEN starts with: {BOT_TOKEN[:10] if BOT_TOKEN else 'None'}")
    print(f"🔍 CHAT_ID is: {CHAT_ID if CHAT_ID else 'None'}")

    # Test the token first
    test_token_alive()

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
