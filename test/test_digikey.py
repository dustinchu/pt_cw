# -*- coding: utf-8 -*
from pyquery import PyQuery
import requests
from time import sleep
import json
import random
import sys
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


def get_two_float(f_str, n):
    f_str = str(f_str)
    a, b, c = f_str.partition('.')

    c = (c + "0" * n)[:n]
    return ".".join([a, c])


# sleep(random.randint(0, 1))
r = requests.get(
    url="https://www.digikey.tw/product-detail/en/hellermanntyton/596-00838/1436-2128-ND/9693606")
# r = requests.get(url=productItemData["productUrl"])
doc = PyQuery(r.text)
attibutes = {}
prices_qty_data = []
datasheet_data = []


non = doc('.product-details-procurement > .product-details-headline')

if doc('.product-details-procurement > .product-details-headline').text()!='Non-Stock':
    print("YY")

print(non.text())
# price
# for price in doc('table[class=product-dollars] > tr').items():
#     price_list = list(price('td').items())
#     if len(price_list) > 0:
#         if (price_list[0].text().strip() != 'Call'):
#             price = {}
#             price_unit = price_list[1].text().strip().replace(
#                 "NT$", "").replace(",", "").replace(" ", "")
#             price_nt = price_list[2].text().strip().replace(
#                 "NT$", "").replace(",", "").replace(" ", "")
#             price_unit = float(price_unit) * 0.97
#             price_nt = float(price_nt) * 0.97
#             price["PRICEBREAK"] = price_list[0].text().strip()
#             price["UNITPRICE"] = get_two_float(f_str=price_unit, n=3)
#             price["EXTENDEDPRICE"] = get_two_float(
#                 f_str=price_nt, n=2)
#             print(price)
