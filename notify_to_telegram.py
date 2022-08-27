# Get my ip address and send it to my email
import requests

from config import telegram_bot_key, telegram_user_id


def send_telegram_message(
    message, user=telegram_user_id, telegram_bot_key=telegram_bot_key
):
    """Send a message to a telegram user with a key"""
    url = "https://api.telegram.org/bot" + telegram_bot_key + "/sendMessage"
    data = {"chat_id": user, "text": message}
    response = requests.post(url, data=data)
    return response
