from flask import Flask
import threading
import time
from quanta_clock import run_clock_alert

app = Flask(__name__)

# 🕒 Background clock function
def clock_worker():
    while True:
        try:
            run_clock_alert()
            time.sleep(10)  # 10 seconds between heartbeats
        except Exception as e:
            print(f"❌ Error in Clock Worker: {e}")
            time.sleep(5)

# 🚀 Start clock in background
threading.Thread(target=clock_worker, daemon=True).start()

@app.route('/')
def home():
    return '🕒 Quanta Clock Worker is running!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
