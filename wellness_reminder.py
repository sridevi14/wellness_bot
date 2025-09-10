import os
import requests
import sys

MY_WEBHOOK = os.getenv("MY_WEBHOOK")
FRIEND_WEBHOOK = os.getenv("FRIEND_WEBHOOK")

def send_message(msg,WEBHOOK_URL):
    if not WEBHOOK_URL:
        print("No webhook configured")
        return
    requests.post(WEBHOOK_URL, json={"text": msg})

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "water"

    messages = {
        "water": "💧 Time to drink some water!",
        "eye": "👀 Eye break! Look away from the screen for 20 seconds.",
        "walk": "🚶 Walking break! Take a 5 min walk.",
        "lunch": "🍴 Lunch break! Relax between 1–2 PM.",
    }
    msg = messages.get(task, "🔔 Reminder!")

    send_message(msg,MY_WEBHOOK)
    if task == "water":
        send_message(msg, FRIEND_WEBHOOK)
