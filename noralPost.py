# -*- coding: utf-8 -*
from pyquery import PyQuery
import requests
from time import sleep
import json
from model.Crawler_vpnData import CrawlerVPNModel
from model.Crawler_name import CrawlerNameModel
from model.Crawler_log import CrawlerLogModel
from model.Crawler_online import CrawlerOnlineModel
import random
import sys
from util.digikey import Digikey
import pymysql
import datetime
import time
pro_name = [
    'Categories',
    'Manufacturer',
    'Series',
    'Packaging',
    'NumberofPositions',
    'NumberofRows',
    'MountingType',
    'ConnectorType',
    'ConnectorStyle',
    'Color',
    'DielectricMaterial',
    'Pitch',
    'Resistance',
    'Tolerance',
    'TurnOffTime',
    'TurnOnTime',
    'CurrentOutput',
    'VoltageOutput',
    'CurrentInput',
    'SupplierDevicePackage',
    'PackageCase',
    'OnStateResistanceMax',
    'LoadCurrent',
    'VoltageLoad',
    'VoltageInput',
    'OutputType',
    'Circuit',
    'CoilResistance',
    'CoilPower',
    'ContactMaterial',
    'TerminationStyle',
    'ReleaseTime',
    'OperateTime',
    'MustReleaseVoltage',
    'MustOperateVoltage',
    'SwitchingVoltage',
    'ContactRatingCurrent',
    'ContactForm',
    'CoilVoltage',
    'CoilCurrent',
    'CapacitanceRange',
    'BasePartNumber',
    'ThicknessMax',
    'NumberofCapacitors',
    'RippleCurrentHighFrequency',
    'RippleCurrentLowFrequency',
    'LifetimeTemp',
    'Type',
    'Specifications',
    'ResistanceOhms',
    'SizeDimension',
    'Features',
    'OperatingTemperature',
    'TemperatureCoefficient',
    'PowerWatts',
    'Style',
    'FlatFlexType',
    'MaterialFlammabilityRating',
    'RowSpacing',
    'ContactFinish',
    'CableTermination',
    'WireGauge',
    'Capacitance',
    'VoltageRated',
    'SeriesName'
    'Category',
    'Producttype',
    'Ratedcurrent',
    'Ratedvoltage',
    'Mountingdirection',
    'Catalog',
    'Numberofpoles',
]

# sleep(random.randint(0, 1))
# r = requests.get(
#     url="https://www.digikey.tw/products/en?keywords=395-024-541-504")
r = requests.get(url="https://www.digikey.com/en/products/detail/stmicroelectronics/M41T00M6F/868914")
# r = requests.get(url=productItemData["productUrl"])
doc = PyQuery(r.text)
attibutes = {}
prices_qty_data = []
datasheet_data = []

# price
for price in doc('table[class=product-dollars] > tr').items():
    price_list = list(price('td').items())
    if len(price_list) > 0:
        if (price_list[0].text().strip() != 'Call'):
            digikey_uril = Digikey()
            price = {}
            price_unit = price_list[1].text().strip().replace(
                "NT$", "").replace(",", "").replace(" ", "")
            price_nt = price_list[2].text().strip().replace(
                "NT$", "").replace(",", "").replace(" ", "")
            price_unit = float(price_unit) * 0.97
            price_nt = float(price_nt) * 0.97
            price["PRICEBREAK"] = price_list[0].text().strip()
            price["UNITPRICE"] = digikey_uril.get_two_float(price_unit, 3)
            price["EXTENDEDPRICE"] = digikey_uril.get_two_float(
                price_nt, 2)
            prices_qty_data.append(price)

# datasheet
for datasheet in doc('.lnkDatasheet').items():
    datasheet_url = datasheet('.lnkDatasheet').attr['href']
    datasheet_name = datasheet('.lnkDatasheet').text()
    if 'digikey' not in datasheet_url:
        datasheet_json = {}
        datasheet_json["name"] = datasheet_name
        datasheet_json["url"] = datasheet_url
        datasheet_data.append(datasheet_json)

# Product Attributes 產品規格
for poduct in doc('table[id=product-attribute-table]').items():
    for att in poduct('tr').items():
        if att('td').text()[:4] != "Type":
            list_title = att('th').text().replace(" ", "").replace(
                "-", "").replace("@",
                                 "").replace(".", "").replace("/", "").replace(
                                     "(", "").replace(")", "")
            # Categories 這邊會有兩行 把兩行存一起
            if att('th').text() == "":
                attibutes['Categories'] += " " + \
                    att('td').text().strip()

            # 詳細規格 名稱當list標題  +內容 寫入
            elif list_title in pro_name:
                attibutes[list_title] = att('td').text().replace("\"",
                                                                 "").strip()
# Categories 會加上 標題  先暫時直接用indexlistname
# attibutes['Categories'] = productItemData['indexListName']
qty = doc('div > .quantity-message').eq(0).text().replace(
    "In Stock", "").replace(",", "").replace(" ", "")
if qty == "":
    attibutes["Stock"] = "-"
else:
    attibutes["Stock"] = qty

descr = "395 SERIES (.100 (2.54MM) CONTA)"

attibutes["HomeName"]="Connectors"

attibutes["PartNumber"]="395-024-541-504"
attibutes["Description"]="ELECTRONIC " + descr
attibutes["MetaDescription"]="-"
digikey_uril=Digikey()

menu=digikey_uril.getManu(Manufacturer = attibutes["Manufacturer"])
# if "nufacturer"]

# attibutes["MetaDescription"]=menu + " " + "395-024-541-504" + " " + attibutes[
#     "Description"] + ", data sheet, SPEC,drawing, inventory& pricing of electronic components ,from  Pingkai Technology CO.,LTD."

attibutes["KeyWords"] = digikey_uril.getKeyWord(
    homename = attibutes["HomeName"],
    partNum = "395-024-541-504",
    Manufacturer = attibutes["Manufacturer"],
    Categories = attibutes['Categories'])

json_data=digikey_uril.check_json_data(attibutes)
json_data["price"]=str(prices_qty_data)
json_data["datasheet"]=str(datasheet_data)
print("manu~~==".format(attibutes["Manufacturer"]))
# url_contents = 'http://develop3.tsg.com.tw/19/p-team/03/path_load.php'
# post_status = requests.post(url_contents, json=json_data)
# print(post_status)
print("---------------------json--------------------------")
print(json_data['Manufacturer'])
print("-----------------------------------------------")

# 'http': "service@pteamtech.com:Pt83109300@{}".format(connect),
# 'https': "service@pteamtech.com:Pt83109300@{}".format(connect)
