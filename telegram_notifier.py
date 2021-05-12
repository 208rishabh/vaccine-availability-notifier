import requests
from config import REQUEST_HEADERS
from config import TELEGRAM_BOT_SEND_MESSAGE_API
import os


token = os.getenv("TELEGRAM_BOT_TOKEN")


def send_message(chat_id, message):
    url = TELEGRAM_BOT_SEND_MESSAGE_API.format(token,chat_id, message)
    requests.get(url, headers=REQUEST_HEADERS)