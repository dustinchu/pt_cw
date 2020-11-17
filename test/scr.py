import requests
import random

username = "dustinchu-country-TW"
password = "a8ab13-f51877-29de8b-aacb4e-0dc6b4"
PROXY_RACK_DNS = "premium.residential.proxyrack.net:{}".format(random.randint(10000,13999))

urlToGet = "https://www.digikey.tw/products/en"

proxy = {"http": "http://{}:{}@{}".format(username, password, PROXY_RACK_DNS),
"https": "https://{}:{}@{}".format(username, password, PROXY_RACK_DNS)}

r = requests.get(urlToGet, proxies=proxy)

print("Response:\n{}".format(r.text))