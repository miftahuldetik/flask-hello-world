from flask import Flask, request
import requests

TOKEN = "7237229468:AAH0QEea9LQkP5XTLNimnI6cPE1AhWrxBmQ"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram Webhook is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    update = request.json
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        # Auto-response example
        reply_text = f"You said: {text}"
        send_message(chat_id, reply_text)

    return {"ok": True}

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
