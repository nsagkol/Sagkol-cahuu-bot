import requests
import time
from bs4 import BeautifulSoup
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = "888024404"
URL = "https://app.cahuu.ch/orders"

last_content = ""

def send_message(text):
    requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

while True:
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")

        content = soup.get_text()

        if content != last_content:
            send_message("⚠️ Änderung erkannt – möglicherweise neuer Auftrag auf Cahuu!")
            last_content = content

    except Exception as e:
        send_message(f"Fehler: {e}")

    time.sleep(2.5)
