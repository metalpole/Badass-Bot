import json
import time
import urllib
import requests

TOKEN = "633569439:AAEfYxsd-ltfZw7tkNKE_Pjewt9ckjIU2xg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
URL2 = https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/last
URL3 = https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:short/last        

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
  
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js
  
def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js
  
def get_bitfinex_updates():
    js = []
    js[0] = get_json_from_url(URL2)
    js[1] = get_json_from_url(URL3)
    return js
    
