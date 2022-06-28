import requests


def send_telegram(text: str):
    token = ''
    url = "https://api.telegram.org/bot"
    channel_id = '@BotIronikaPhoto'
    url += token
    method = url + "/sendMessage"

    requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })


