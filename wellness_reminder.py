import os
import requests
import sys

WEBHOOK_URL = os.getenv("GCHAT_WEBHOOK")

def send_message(msg):
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

    send_message(messages.get(task, "🔔 Reminder!"))
