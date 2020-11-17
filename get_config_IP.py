from model.Crawler_VpnData import CrawlerVPNModel
import requests
from time import sleep
from pyquery import PyQuery
import pymysql

html = requests.get('https://nordvpn.com/zh-tw/ovpn/', timeout=10)
i = 0
if html.status_code == 200:
    doc = PyQuery(html.text)
    for listitem in doc('.ListItem').items():
        item_name = listitem('.mr-2').text()
        print(item_name)
        try:
            proxy = {
                'http':
                "service@pteamtech.com:Pt83109300@{item}:80".
                format(item=item_name),
                'https':
                "service@pteamtech.com:Pt83109300@{item}:80".
                format(item=item_name)
            }
            html = requests.get('https://www.digikey.tw/products/en',
                                proxies=proxy)
            if html.status_code == 200:
                x = proxy['http'].split('@', 2)
                vpn_name = CrawlerVPNModel.select_conndctData(x[2])
                if vpn_name == []:
                    json_data = {}
                    json_data['connectData'] = x[2]
                    json_data['county'] = 'openPublic'
                    user = CrawlerVPNModel(**json_data)
                    user.save_to_db()
                    print(proxy)
        except:
            print("error name ==={item_name}".format(item_name=item_name))
