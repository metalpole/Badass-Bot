import json
import time
import urllib
import requests
import random
from dbhelper import DBHelper

db = DBHelper()
TOKEN = "605773092:AAGbLA78D8cmcFUJyLvzLRbvnhN_TqxwWCI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
greetings = {1: "I hear you 110% man", 2: "I'm listening", 3: "I feel you bro",
             4: "Go on", 5: "Hmmm", 6: "yup"}


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            if "eden" in text.lower():
                send_message("Thank you so much for your donation of ETH. The EdenChain team wishes you all the best in trying to get a refund of your ETH deposit. Do learn to put your remaining fiat to better use. Cheers!", chat)
            elif len(text) > 20:
                send_message(greetings[random.randint(1,5)], chat)
        except Exception as e:
            print(e)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(3)


if __name__ == '__main__':
    main()
