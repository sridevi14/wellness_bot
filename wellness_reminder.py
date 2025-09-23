import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv()

MY_WEBHOOK = os.getenv("MY_WEBHOOK")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(msg,WEBHOOK_URL):
    if not WEBHOOK_URL:
        print("No webhook configured")
        return
    requests.post(WEBHOOK_URL, json={"text": msg})


def send_telegram_message(msg, token, chat_id):
    if not token or not chat_id:
        print("No Telegram credentials configured")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": msg}
    requests.post(url, json=payload)
if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "water"

    messages = {
        "water": "💧 Time to drink!",
        "eye": "👀 Eye break! Look away from the screen for 20 seconds.",
        "walk": "🚶 Walking break! Take a 5 min walk.",
        "lunch": "🍴 Lunch break! Relax between 1–2 PM.",
    }
    msg = messages.get(task, "🔔 Reminder!")

    send_message(msg,MY_WEBHOOK)
    # if task == "water":
        # send_telegram_message(msg, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
