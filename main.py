from quanta_clock import run_clock_alert
import time

if __name__ == "__main__":
    while True:
        try:
            run_clock_alert()
            time.sleep(10)  # Wait 10 seconds before the next clock alert
        except Exception as e:
            print(f"❌ Error in clock loop: {e}")
            time.sleep(5)  # Wait 5 seconds before retrying if error
