import requests
from config import API_KEY

def gpt_text (message_fromuser):
    url = "https://api.air.fail/public/text/chatgpt"
    boby = {"model": "gpt-4", "content": message_fromuser}
    headers = {"Authorization": API_KEY}
    response = requests.post(url, headers=headers, json=boby)
    data = response.json()
    content_value = data [0]. get("content", None)
    return content_value
    