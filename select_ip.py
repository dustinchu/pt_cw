from model.Crawler_VpnData import CrawlerVPNModel
import requests
from time import sleep
import pymysql
vpn = [
#     {
#     'name': 'ua',
#     'county': 'Albania',
#     'start': 1,
#     'end': 1000
# },   {
#     'name': 'tw',
#     'county': 'Albania',
#     'start': 1,
#     'end': 1000
# },  {
#     'name': 'jp',
#     'county': 'Albania',
#     'start': 1,
#     'end': 1000
# },]
    {
    'name': 'al',
    'county': 'Albania',
    'start': 1,
    'end': 1000
}, {
    'name': 'ar',
    'county': 'Argentina',
    'start': 1,
    'end': 1000
}, {
    'name': 'au',
    'county': 'Australia',
    'start': 1,
    'end': 1000
}, {
    'name': 'at',
    'county': 'Austria',
    'start': 1,
    'end': 1000
}, {
    'name': 'be',
    'county': 'Belgium',
    'start': 1,
    'end': 1000
}, {
    'name': 'ba',
    'county': 'Bosnia and Herzegovina',
    'start': 1,
    'end': 1000
}, {
    'name': 'br',
    'county': 'Brazil',
    'start': 1,
    'end': 1000
}, {
    'name': 'bg',
    'county': 'Bulgaria',
    'start': 1,
    'end': 1000
}, {
    'name': 'ca',
    'county': 'Canada',
    'start': 1,
    'end': 1000
}, {
    'name': 'cl',
    'county': 'Chile',
    'start': 1,
    'end': 1000
}, {
    'name': 'cr',
    'county': 'Costa Rica',
    'start': 1,
    'end': 1000
}, {
    'name': 'hr',
    'county': 'Croatia',
    'start': 1,
    'end': 1000
}, {
    'name': 'cy',
    'county': 'Cyprus',
    'start': 1,
    'end': 1000
}, {
    'name': 'cz',
    'county': 'Czech',
    'start': 1,
    'end': 1000
}, {
    'name': 'dk',
    'county': 'Denmark',
    'start': 1,
    'end': 1000
}, {
    'name': 'ee',
    'county': 'Estonia',
    'start': 1,
    'end': 1000
}, {
    'name': 'fi',
    'county': 'Finland',
    'start': 1,
    'end': 1000
}, {
    'name': 'fr',
    'county': 'France',
    'start': 1,
    'end': 1000
}, {
    'name': 'ge',
    'county': 'Georgia',
    'start': 1,
    'end': 1000
}, {
    'name': 'de',
    'county': 'Germany',
    'start': 1,
    'end': 1000
}, {
    'name': 'gr',
    'county': 'greece',
    'start': 1,
    'end': 1000
}, {
    'name': 'hk',
    'county': 'Hong county Kong',
    'start': 1,
    'end': 1000
}, {
    'name': 'hu',
    'county': 'Hungary',
    'start': 1,
    'end': 1000
}, {
    'name': 'is',
    'county': 'iceland',
    'start': 1,
    'end': 1000
}, {
    'name': 'in',
    'county': 'india',
    'start': 1,
    'end': 1000
}, {
    'name': 'id',
    'county': 'indonesia',
    'start': 1,
    'end': 1000
}, {
    'name': 'ie',
    'county': 'ireland',
    'start': 1,
    'end': 1000
}, {
    'name': 'il',
    'county': 'israel',
    'start': 1,
    'end': 1000
}, {
    'name': 'it',
    'county': 'italy',
    'start': 1,
    'end': 1000
}, {
    'name': 'jp',
    'county': 'japan',
    'start': 1,
    'end': 1000
}, {
    'name': 'lv',
    'county': 'latvia',
    'start': 1,
    'end': 1000
}, {
    'name': 'lu',
    'county': 'luxembourg',
    'start': 1,
    'end': 1000
}, {
    'name': 'my',
    'county': 'malaysia',
    'start': 1,
    'end': 1000
}, {
    'name': 'mx',
    'county': 'mexico',
    'start': 1,
    'end': 1000
}, {
    'name': 'md',
    'county': 'moldova',
    'start': 1,
    'end': 1000
}, {
    'name': 'nl',
    'county': 'netherlands',
    'start': 1,
    'end': 1000
}, {
    'name': 'nz',
    'county': 'new county zealand',
    'start': 1,
    'end': 1000
}, {
    'name': 'mk',
    'county': 'north county Macedonia',
    'start': 1,
    'end': 1000
}, {
    'name': 'no',
    'county': 'Norway',
    'start': 1,
    'end': 1000
}, {
    'name': 'pl',
    'county': 'poland',
    'start': 1,
    'end': 1000
}, {
    'name': 'pt',
    'county': 'portugal',
    'start': 1,
    'end': 1000
}, {
    'name': 'ro',
    'county': 'romania',
    'start': 1,
    'end': 1000
}, {
    'name': 'rs',
    'county': 'serbia',
    'start': 1,
    'end': 1000
}, {
    'name': 'sg',
    'county': 'singapore',
    'start': 1,
    'end': 1000
}, {
    'name': 'sk',
    'county': 'slovakia',
    'start': 1,
    'end': 1000
}, {
    'name': 'si',
    'county': 'slovenia',
    'start': 1,
    'end': 1000
}, {
    'name': 'za',
    'county': 'south Africa',
    'start': 1,
    'end': 1000
}, {
    'name': 'kr',
    'county': 'Korea',
    'start': 1,
    'end': 1000
}, {
    'name': 'es',
    'county': 'Spain',
    'start': 1,
    'end': 1000
}, {
    'name': 'se',
    'county': 'Sweden',
    'start': 1,
    'end': 1000
}, {
    'name': 'ch',
    'county': 'Switzerland',
    'start': 1,
    'end': 1000
}, {
    'name': 'tw',
    'county': 'Taiwan',
    'start': 1,
    'end': 1000
}, {
    'name': 'th',
    'county': 'Thailand',
    'start': 1,
    'end': 1000
}, {
    'name': 'tr',
    'county': 'Turkey',
    'start': 1,
    'end': 1000
}, {
    'name': 'ua',
    'county': 'Ukraine',
    'start': 1,
    'end': 1000
}, {
    'name': 'uk',
    'county': 'Kingdom',
    'start': 1,
    'end': 1000
}, {
    'name': 'us',
    'county': 'United States',
    'start': 1,
    'end': 10000
}, {
    'name': 'vn',
    'county': 'Vietnam',
    'start': 1,
    'end': 1000
}]

while True:
    for vpnItem in vpn:
        print(vpnItem['name'], vpnItem['county'])
        for i in range(vpnItem['start'], vpnItem['end']):

            try:
                proxy = {
                    'http':
                    "service@pteamtech.com:Pt83109300@{item}{conut}.nordvpn.com:80"
                    .format(item=vpnItem['name'], conut=i),
                    'https':
                    "service@pteamtech.com:Pt83109300@{item}{conut}.nordvpn.com:80"
                    .format(item=vpnItem['name'], conut=i)
                }
                html = requests.get('https://www.digikey.tw/products/en',
                                    proxies=proxy)
                if html.status_code == 200:
                    x = proxy['http'].split('@', 2)
                    vpn_name = CrawlerVPNModel.select_conndctData(x[2])
                    if vpn_name == []:
                        json_data = {}
                        json_data['connectData'] = x[2]
                        json_data['county'] = vpnItem['county']
                        user = CrawlerVPNModel(**json_data)
                        user.save_to_db()
                        print(proxy)
            except:
                print("error restart==={count} name ==={proxy}".format(
                    count=i, proxy=vpnItem['name']))
    # sleep(32000)

# proxy = {
#     'http': "service@pteamtech.com:Pt83109300@jp518.nordvpn.com:80",
#     'https': "service@pteamtech.com:Pt83109300@jp518.nordvpn.com:80"
# }
# html = requests.get('https://www.digikey.tw/products/en',
#                     proxies=proxy, timeout=10)
# if html.status_code == 200:
#     x = proxy['http'].split('@',2)
#     vpn_name = CrawlerVPNModel.select_conndctData(x[2])
#     if vpn_name == []:
#         json_data={}
#         json_data['connectData']=x[2]
#         json_data['county']= 1
#         user = CrawlerVPNModel(**json_data)
#         user.save_to_db()
#         print(proxy)