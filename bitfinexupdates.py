import json
import time
import urllib
import requests

TOKEN = "633569439:AAEfYxsd-ltfZw7tkNKE_Pjewt9ckjIU2xg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
URL2 = "https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/last"
URL3 = "https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:short/last" 

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

def get_last_chat_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return chat_id
    
def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
def get_bitfinex_updates():
    js1 = get_json_from_url(URL2)
    js2 = get_json_from_url(URL3)
    return (js1, js2)

def main():
    while True:
        chat = get_last_chat_id(get_updates())
        js1, js2 = get_bitfinex_updates()
        long, short = (js1[1], js2[1])
        send_message("Longs = " + str(long) + ", Shorts = " + str(short), chat)
        time.sleep(60)
        
if __name__ == '__main__':
    main()
