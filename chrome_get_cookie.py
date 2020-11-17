# -*- coding: utf-8 -*
from pyquery import PyQuery
import requests
from time import sleep
import json
import random
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile
import os
from model.Crawler_cookie import CrawlerCookieModel


def proxy_chrome(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
    manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%(host)s",
                port: parseInt(%(port)d)
              },
              bypassList: ["foobar.com"]
            }
          };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(user)s",
                password: "%(pass)s"
            }
        };
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
        """ % {
        "host": PROXY_HOST,
        "port": PROXY_PORT,
        "user": PROXY_USER,
        "pass": PROXY_PASS,
    }

    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    co = Options()
    # extension support is not possible in incognito mode for now
    # co.add_argument('--incognito')
    # co.add_argument('--headless')
    co.add_argument('--disable-gpu')
    # disable infobars
    co.add_argument('--disable-infobars')
    co.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors"])
    # location of chromedriver, please change it according to your project.
    co.add_extension(pluginfile)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=co)
    # driver = webdriver.Chrome('./chromedriver', chrome_options=co)
    # return the driver with added proxy configuration.
    return driver


username = "pteamtech"
password = "76bb3b-357e9e-4492c2-d52f43-35690e"

while True :

    sleep(10)
    try:
        driver = proxy_chrome('megaproxy.rotating.proxyrack.net',
                            random.randint(10000, 13999), username, password)
        driver.get("https://www.digikey.tw/product-detail/en/edac-inc/333-062-500-203/151-333-062-500-203-ND/10896386")
        # driver.get('https://httpbin.org/headers')
        html_source = driver.page_source
        digikey_cookie = {}
        sec = 0
        while True:
            doc = PyQuery(driver.page_source)
            doc_title = doc('title').text()
            if doc_title == "Challenge Validation":
                sleep(1)
                print(doc('title').text(),sec)
                sec += 1
                # html_source = driver.page_source
                # with open('webpage.html', 'w', encoding="utf-8") as f:
                #     f.write(html_source)
                if sec ==150:
                    driver.close()
                    driver.quit()
                    break
            else:
                print("sleep")
                sleep(10)
                print("sleep 5 sec  exit")
                cookie = driver.get_cookies()

                driver.close()
                driver.quit()
                for c in cookie:
                    digikey_cookie[c['name']] = c['value']
                print("-------------\n{}\n---------------".format(digikey_cookie))
                cookie = '_gcl_au=1.1.1630470618.1603957343; TS01c48c64={TS01c48c64}; TS0132ff3a={TS0132ff3a}; _evga_6ce7=36a28663b60fff93.; dkuhint=false; TS018ea5c6={TS018ea5c6}; _ga=GA1.2.1727094265.1603957604; _gid=GA1.2.130502340.1603957604; EG-U-ID={EG}; EG-S-ID={EG2}; csscxt={csscxt}; QSI_SI_9nMMPDqA0H0NQxf_intercept=true; QSI_HistorySession=https%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2F20~1603957604506%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2Fcard-edge-connectors-edgeboard-connectors%2F303%3FFV%3D-8%257C791%26quantity%3D0%26ColumnSort%3D0%26page%3D311%26pageSize%3D500~1603957621059%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproduct-detail%2Fen%2Fedac-inc%2F333-062-500-203%2F151-333-062-500-203-ND%2F10896386~1603957629145%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2Fcard-edge-connectors-edgeboard-connectors%2F303%3FFV%3D-8%257C791%26quantity%3D0%26ColumnSort%3D0%26page%3D311%26pageSize%3D500~1603957654621%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproduct-detail%2Fen%2Fedac-inc%2F333-062-500-203%2F151-333-062-500-203-ND%2F10896386~1603957675851; _uetsid=542eac00198d11eba6d937612098a0e4; _uetvid=ddc9f92d9fa9b4deaf4ae7c82132c790; ak_bmsc={ak_bmsc}; bm_sz={bm_sz}; sid={sid}; TS017613a9={TS017613a9}; TS018060f7={TS018060f7}; _abck={_abck}; bm_mi={bm_mi}; TS01d5128f={TS01d5128f}; RT={RT}; ps-eudo-sid={ps}; TS013c3a0b={TS013c3a0b}; utag_main={utag_main}; bm_sv={bm_sv} '.format(TS01c48c64=digikey_cookie[
                    'TS01c48c64'], TS0132ff3a=digikey_cookie['TS0132ff3a'], TS018ea5c6=digikey_cookie['TS018ea5c6'], EG=digikey_cookie['EG-U-ID'], EG2=digikey_cookie['EG-U-ID'], csscxt=digikey_cookie['csscxt'], ak_bmsc=digikey_cookie['ak_bmsc'], bm_sz=digikey_cookie['bm_sz'], sid=digikey_cookie['sid'], TS017613a9=digikey_cookie['TS017613a9'], TS018060f7=digikey_cookie['TS018060f7'], _abck=digikey_cookie['_abck'], bm_mi=digikey_cookie['bm_mi'], TS01d5128f=digikey_cookie['TS01d5128f'], RT=digikey_cookie['RT'], ps=digikey_cookie['ps-eudo-sid'], TS013c3a0b=digikey_cookie['TS013c3a0b'], utag_main=digikey_cookie['utag_main'], bm_sv=digikey_cookie['bm_sv'])

                print(cookie)
                sql_json_arr={}
                sql_json_arr['cookie']=cookie
                crw_log_data = CrawlerCookieModel(**sql_json_arr)
                crw_log_data.save_to_db()
                break
    except:
        print("error")
# target_headers1 = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#     'Accept': '*/*',
#     'Referer': 'https://www.digikey.com/products/en',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cookie': cookie,
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
# }
# username = "pteamtech"
# password = "76bb3b-357e9e-4492c2-d52f43-35690e"
# PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:{}".format(
#     random.randint(10000, 13999))

# proxy = {
#     "http": "http://{}:{}@{}".format(username, password,
#                                      PROXY_RACK_DNS),
#     "https": "https://{}:{}@{}".format(username, password,
#                                        PROXY_RACK_DNS)
# }
# r = requests.get(url="https://www.digikey.tw/product-detail/en/mallory-sonalert-products-inc/ACC03/458-1109-ND/1643709",
#                  headers=target_headers1, proxies=proxy)
# print(r.text)

#             #     crw_log_data = CrawlerFirstModel(**sql_json_arr)
#             #     crw_log_data.save_to_db()
