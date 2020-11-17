# -*- coding: utf-8 -*
from pyquery import PyQuery
import requests
from time import sleep
import json
# from model.Crawler_vpnData import CrawlerVPNModel
from model.Crawler_name import CrawlerNameModel
from model.Crawler_log import CrawlerLogModel
from model.Crawler_online import CrawlerOnlineModel
# from model.Crawler_runSec import CrawlerRunSecModel
from model.Crawler_data import CrawlerFirstModel
import random
import sys
from util.digikey import Digikey
from util.line import LINE
import pymysql
import datetime
import time
target_headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.digikey.com/products/en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
start_digiket_url = "https://www.digikey.tw/products/en"
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


class DigiketScraper():
    def homePage(self, home_url, proxy, crw_list):
        print(home_url)
        r = requests.get(url=home_url, headers=target_headers, proxies=proxy)
        doc = PyQuery(r.text)
        if r.status_code == 200:
            # 第一頁列表 得到標題 跟超連結
            for home_list in doc('.indexNewIndicator > a').items():
                home = {}
                home_name = home_list.text()
                home_url = "https://www.digikey.tw" + home_list.attr['href']
                home["home_name"] = home_name
                home["home_url"] = home_url

                if home_name in crw_list['crwName']:
                    print("看一下home==={}".format(home))
                    self.homeIndexList(homedata=home,
                                       proxy=proxy,
                                       crw_list=crw_list)
            # break
        else:
            print("網址失效", home_url)

    # ?FV=-8%7C1010&quantity=0&ColumnSort=0&page=1&pageSize=500

    def homeIndexList(self, homedata, proxy, crw_list):
        count_index = 1
        crw_start_name = crw_list['listName']
        print("url==={}".format(homedata["home_url"]))
        body_r = requests.get(url=homedata["home_url"],
                              headers=target_headers,
                              proxies=proxy)
        body_doc = PyQuery(body_r.text)
        if body_r.status_code == 200:
            for body_list in body_doc('.catfiltersub > li').items():
                body_url = "https://www.digikey.tw" + body_list(
                    'a').attr['href']
                body_name = body_list('a').text()

                crw_list_name = CrawlerOnlineModel.select_crwOnline(
                    crwTitle=crw_list['crwName'], index=crw_list['category'])
                # 沒資料將第一筆寫入
                if crw_list_name == []:
                    online_json = {}
                    online_json['crwTitle'] = crw_list['crwName']
                    online_json['crwName'] = crw_list['listName']
                    online_json['partNum'] = 'frist'
                    online_json['page'] = crw_list['sPage']
                    online_json['onlineIndex'] = crw_list['category']
                    onlineModel = CrawlerOnlineModel(**online_json)
                    onlineModel.save_to_db()
                else:
                    crw_start_name = crw_list_name[0]['crwName']

                if crw_start_name == body_name:
                    print("開始抓取 {home}  ----->{body_name}".format(
                        home=homedata["home_name"], body_name=body_name))

                    homeIndex = {}
                    homeIndex["home_name"] = homedata["home_name"]
                    homeIndex["home_url"] = homedata["home_url"]
                    homeIndex["indexListName"] = body_name
                    homeIndex["indexListUrl"] = body_url
                    homeIndex["count"] = count_index
                    self.productList(indexList=homeIndex,
                                     proxy=proxy,
                                     crw_list=crw_list,
                                     crw_list_name=crw_list_name)
                count_index += 1
                # break
        else:
            print("網址失效{}".format(homedata["home_url"]))

    def productList(self, indexList, proxy, crw_list, crw_list_name):
        crwStatus = False
        ePageCount = 1
        sPageCount = 1
        if crw_list["pageStatus"] == 'Y':
            ePageCount = crw_list['ePage']
            sPageCount = crw_list['sPage']
        else:
            ePageCount = 50000
            sPageCount = 1
        if crw_list_name != []:
            sPageCount = crw_list_name[0]['page']
        print('準備從第{}頁開始爬資料'.format(sPageCount))
        for i in range(int(ePageCount)):
            crw_page = int(sPageCount) + i
            body_url = indexList[
                'indexListUrl'] + "?FV=-8%7C791&quantity=0&ColumnSort=0&page={pageno}&pageSize=500"
            print("body_url====={}".format(body_url))
            body_url = body_url.format(pageno=crw_page)
            data_r = requests.get(url=body_url,
                                  headers=target_headers,
                                  proxies=proxy)
            # data_r = requests.get(url=body_url, headers=headers)
            if data_r.status_code == 200:
                productDoc = PyQuery(data_r.text)

                itemno = 1
                print(body_url)
                if len(list(productDoc('table tr').items())) != 2:
                    # print(len(list(productDoc('table tr').items())))
                    for productList in productDoc('table tr').items():
                        productListData = {}
                        # 產品頁 URL
                        productUrl = productList(
                            '.tr-dkPartNumber > a').attr['href']
                        if (productUrl is not None):
                            # print(productUrl)
                            trs = list(productList('td').items())
                            if len(trs) > 0:
                                if trs[3].text().strip() != "":
                                    partNum = trs[4].text().strip()
                                    # 判斷一下 從上一次最後一筆開始撈
                                    crw_list_name = CrawlerOnlineModel.select_crwOnline(
                                        crwTitle=crw_list['crwName'],
                                        index=crw_list['category'])
                                    if crw_list_name == []:
                                        crwStatus = True
                                    else:
                                        if crw_list_name[0][
                                                'partNum'] == 'frist' or crw_list_name[
                                                    0]['partNum'] == partNum:
                                            crwStatus = True
                                    # 找到上一次撈取的資料後 在開始爬
                                    if crwStatus:
                                        productListData[
                                            "homeName"] = indexList[
                                                "home_name"]
                                        productListData["homeUrl"] = indexList[
                                            "home_url"]
                                        productListData[
                                            "indexListName"] = indexList[
                                                "indexListName"]
                                        productListData[
                                            "indexListUrl"] = indexList[
                                                "indexListUrl"]
                                        productListData["count"] = indexList[
                                            "count"]
                                        # 製造商零件編號
                                        productListData["PartNumber"] = partNum
                                        # 描述
                                        productListData["Description"] = trs[
                                            6].text().strip()
                                        # 數量
                                        qty = trs[7].text().strip()
                                        productListData["qty"] = qty[:qty.
                                                                     find(" ")]
                                        productListData[
                                            "productUrl"] = "https://www.digikey.tw" + productUrl
                                        self.productData(
                                            productItemData=productListData,
                                            proxy=proxy,
                                            crw_page=crw_page,
                                            crw_list=crw_list)
                        else:
                            # 前兩筆會是null 第三筆還是null 跳出
                            if (itemno == 3):
                                break
                        itemno += 1

                # 沒資料 代表這頁沒東西 直接跳出 換下一個listname 撈取
                else:
                    crw_name_json = CrawlerNameModel.select_crwname(
                        crwName=crw_list['crwName'],
                        category=crw_list['category'])
                    json_name_index = 0
                    for json_name in crw_name_json:
                        json_name_index += 1
                        if json_name["listName"] == crw_list['listName']:
                            break
                    try:
                        crw_name_json[json_name_index]
                        CrawlerOnlineModel.update_crwOnline(
                            crwTitle=crw_list['crwName'],
                            crwName=crw_list['listName'],
                            page=crw_list['sPage'],
                            partNum='frist',
                            index=crw_list['category'])
                    except:
                        CrawlerOnlineModel.delete_crwOnline(
                            crwTitle=crw_list['crwName'],
                            crwName=crw_list['listName'],
                            index=crw_list['category'])
                    break

            # # 測試跑一圈就好
            # break

    def productData(self, productItemData, proxy, crw_page, crw_list):
        crw_sec = 0
        post_sec = 0
        tStart = time.time()  # 計時開始
        digikey_uril = Digikey()
        send_line = LINE()
        proxy_msg = proxy_ip()
        # sleep(random.randint(0, 1))
        r = requests.get(url=productItemData["productUrl"],
                         headers=target_headers,
                         proxies=proxy)
        # r = requests.get(url=productItemData["productUrl"])
        doc = PyQuery(r.text)
        attibutes = {}
        prices_qty_data = []
        datasheet_data = []

        # if doc('.product-details-procurement > .product-details-headline').text() != 'Non-Stock':
        # price
        for price in doc('table[class=product-dollars] > tr').items():
            price_list = list(price('td').items())
            if len(price_list) > 0:
                if (price_list[0].text().strip() != 'Call'):
                    try:
                        price = {}
                        price_unit = price_list[1].text().strip().replace(
                            "NT$", "").replace(",", "").replace(" ", "")
                        price_nt = price_list[2].text().strip().replace(
                            "NT$", "").replace(",", "").replace(" ", "")
                        price_unit = float(price_unit) * 0.97
                        price_nt = float(price_nt) * 0.97
                        price["PRICEBREAK"] = price_list[0].text().strip()
                        price["UNITPRICE"] = digikey_uril.get_two_float(
                            price_unit, 3)
                        price["EXTENDEDPRICE"] = digikey_uril.get_two_float(
                            price_nt, 2)
                        prices_qty_data.append(price)
                    except:
                        try:
                            price = {}
                            price_unit = price_list[1].text().strip().replace(
                                "NT$", "").replace(",", "").replace(" ", "")
                            price_nt = price_list[2].text().strip().replace(
                                "NT$", "").replace(",", "").replace(" ", "")
                            price_unit = float(price_unit) * 0.97
                            price_nt = float(price_nt) * 0.97
                            price["PRICEBREAK"] = price_list[0].text().strip()
                            price["UNITPRICE"] = digikey_uril.get_two_float(
                                price_unit, 3)
                            price["EXTENDEDPRICE"] = digikey_uril.get_two_float(
                                price_nt, 2)
                            prices_qty_data.append(price)
                        except BaseException as e:
                            send_line.lineNotifyMessage(
                                "{}\nBaseException!! \n{}".format(productItemData["productUrl"], e))
                            return 0

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
                        "-", "").replace("@", "").replace(".", "").replace(
                            "/", "").replace("(", "").replace(")", "")
                    # Categories 這邊會有兩行 把兩行存一起
                    if att('th').text() == "":
                        attibutes['Categories'] += " " + \
                            att('td').text().strip()

                    # 詳細規格 名稱當list標題  +內容 寫入
                    elif list_title in pro_name:
                        attibutes[list_title] = att('td').text().replace(
                            "\"", "").strip()
        # Categories 會加上 標題  先暫時直接用indexlistname
        # attibutes['Categories'] = productItemData['indexListName']
        qty = doc('div > .quantity-message').eq(0).text().replace(
            "In Stock", "").replace(",", "").replace(" ", "")
        if qty == "":
            attibutes["Stock"] = "-"
        else:
            attibutes["Stock"] = qty

        if productItemData["homeName"] == "Connectors, Interconnects":
            attibutes["HomeName"] = "Connectors"
        else:
            attibutes["HomeName"] = productItemData["homeName"]

        attibutes["PartNumber"] = productItemData["PartNumber"]
        attibutes[
            "Description"] = "ELECTRONIC " + productItemData["Description"]
        attibutes["MetaDescription"] = "-"
        menu = digikey_uril.getManu(Manufacturer=attibutes["Manufacturer"])

        attibutes["Manufacturer"] = digikey_uril.getManufacturer(
            Manufacturer=attibutes["Manufacturer"])
        # if "-" in attibutes["Manufacturer"]:
        #     menu = attibutes["Manufacturer"][0:attibutes["Manufacturer"].find("-")]
        # elif " " in attibutes["Manufacturer"]::
        #     menu = attibutes["Manufacturer"][0:attibutes["Manufacturer"].find(" ")]
        # else:
        #     menu = attibutes["Manufacturer"]

        attibutes["MetaDescription"] = menu + " " + productItemData[
            "PartNumber"] + " " + attibutes[
                "Description"] + ", data sheet, SPEC,drawing, inventory& pricing of electronic components ,from  Pingkai Technology CO.,LTD."
        attibutes["KeyWords"] = digikey_uril.getKeyWord(
            homename=attibutes["HomeName"],
            partNum=productItemData["PartNumber"],
            Manufacturer=attibutes["Manufacturer"],
            Categories=attibutes['Categories'])

        

        json_data = digikey_uril.check_json_data(attibutes)
        if prices_qty_data == []:
            json_data["price"] = "-"
        else:
            json_data["price"] = str(prices_qty_data)

        if datasheet_data == []:
            json_data["datasheet"] = "-"
        else:
            json_data["datasheet"] = str(datasheet_data)

        tEnd = time.time()  # 計時結束
        crw_sec = tEnd - tStart
        print("product %f sec" % (tEnd - tStart))  # 會自動做近位
        # print("---------------------json--------------------------")
        # print(json_data)
        # print("-----------------------------------------------")
        # url_contents = 'http://demo5.tsg.com.tw/19/p-team/path_load.php'
        # try:
        # tStart = time.time()  # 計時開始
        # post_status = requests.post(url_contents, json=json_data)
        # tEnd = time.time()  # 計時結束
        # post_sec = tEnd - tStart
        # print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位
        # 儲存耗費時間
        # sec_json = {}
        # x = datetime.datetime.now()
        # date = str(x.year) + str(x.month) + str(x.day)
        # sec_json["partNum"] = productItemData["PartNumber"]
        # sec_json["crwSec"] = str(crw_sec)
        # sec_json["postSec"] = str(post_sec)
        # sec_json["date"] = date
        # log = CrawlerRunSecModel(**sec_json)
        # log.save_to_db()
        # except:
        #     send_line.lineNotifyMessage("{}\n{}\n 傳資料到網站發生錯誤!!!".format(
        #         "http://demo5.tsg.com.tw/19/p-team/path_load.php",
        #         json_data))
        # if post_status.text[10:len(post_status.text) - 1]:
        # print(
        #     "ok   Categories: {Categories}   PartNumber: {PartNumber}    keyword:{keyword}".
        #     format(Categories=json_data["Categories"],
        #            PartNumber=json_data["PartNumber"],
        #            keyword=attibutes["KeyWords"]))
        tStart = time.time()  # 計時開始
        # log_result = CrawlerLogModel.select_crwlog(
        #     crwName=productItemData['indexListName'],
        #     crwIndex=crw_list['category'])

        # # 更新每天爬的數量
        # if log_result != []:
        #     CrawlerLogModel.update_crwlog(
        #         crwName=productItemData['indexListName'],
        #         count=log_result[0]["count"] + 1,
        #         crwIndex=crw_list['category'])
        # else:
        #     log_json = {}
        #     x = datetime.datetime.now()
        #     date = str(x.year) + str(x.month) + str(x.day)
        #     log_json["crwTitle"] = attibutes["HomeName"]
        #     log_json["crwName"] = productItemData['indexListName']
        #     log_json["count"] = "1"
        #     log_json["crwDate"] = date
        #     log_json["crwIndex"] = crw_list['category']
        #     log = CrawlerLogModel(**log_json)
        #     log.save_to_db()

        CrawlerOnlineModel.update_crwOnline(
            crwTitle=productItemData['homeName'],
            crwName=productItemData['indexListName'],
            page=crw_page,
            partNum=json_data["PartNumber"],
            index=crw_list['category'])

        data = CrawlerFirstModel.find_by_name(attibutes["PartNumber"])
        j, s = digikey_uril.get_data_body(
            digikey_uril.check_json_data(attibutes))
        sql_json_arr = j
        sql_json_arr["body"] = str(s)
        sql_json_arr["price"] = str(prices_qty_data)
        sql_json_arr["datasheet"] = str(datasheet_data)
        if doc('.product-details-procurement > .product-details-headline').text() != 'Non-Stock':
            sql_json_arr['status'] = "NULL"
        else:
            sql_json_arr['status'] = "non-Stock"
        crw_log_data = CrawlerFirstModel(**sql_json_arr)
        crw_log_data.save_to_db()
        if data == []:
            crw_log_data = CrawlerFirstModel(**sql_json_arr)
            crw_log_data.save_to_db()
        else:
            print("update==={}".format(CrawlerFirstModel.update_to_db(
                id=data[0]['id'], sql_json_arr=sql_json_arr)))
        # 計時結束
        tEnd = time.time()
        post_sec = tEnd - tStart
        print("inset update %f sec" % (tEnd - tStart))  # 會自動做近位
        # else:
        #     send_line.lineNotifyMessage(
        #         "{}\n  傳資料到網站發生錯誤 \n status !=200".format(
        #             "http://demo5.tsg.com.tw/19/p-team/path_load.php"))
        #     print("資料傳到網站出現錯誤!!")
        # else:
        #     # 沒上架的資料
        #     data = CrawlerFirstModel.find_by_name(attibutes["PartNumber"])
        #     j, s = digikey_uril.get_data_body(
        #         digikey_uril.check_json_data(attibutes))
        #     sql_json_arr = j
        #     sql_json_arr["body"] = str(s)
        #     sql_json_arr["price"] = str(prices_qty_data)
        #     sql_json_arr["datasheet"] = str(datasheet_data)
        #     sql_json_arr['status'] = "non-Stock"
        #     if data == []:
        #         crw_log_data = CrawlerFirstModel(**sql_json_arr)
        #         crw_log_data.save_to_db()
        #     else:
        #         print("update==={}".format(CrawlerFirstModel.update_to_db(
        #             id=data[0]['id'], sql_json_arr=sql_json_arr)))


class proxy_ip():
    def getConnectProxy(self):
        username = "pteamtech"
        password = "76bb3b-357e9e-4492c2-d52f43-35690e"
        PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:{}".format(
            random.randint(10000, 13999))
        # PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:222"

        proxy = {
            "http": "http://{}:{}@{}".format(username, password,
                                             PROXY_RACK_DNS),
            "https": "https://{}:{}@{}".format(username, password,
                                               PROXY_RACK_DNS)
        }
        return proxy


if __name__ == '__main__':

    cra_nama = sys.argv[1]
    index = sys.argv[2]
    print("開始撈取 : {}---------index:{}".format(str(cra_nama), str(index)))
    scraper = DigiketScraper()
    proxy_msg = proxy_ip()
    proxy = ""
    # proxy = {
    #     'http': "service@pteamtech.com:Pt83109300@ua31.nordvpn.com:80",
    #     'https': "service@pteamtech.com:Pt83109300@ua31.nordvpn.com:80"
    # }
    print("使用==={proxy}".format(proxy=proxy))
    while True:
        try:
            proxy = proxy_msg.getConnectProxy()
            print(proxy)
            html = requests.get('https://www.digikey.tw/products/en',
                                proxies=proxy,
                                headers=target_headers)
            if html.status_code == 200:

                for crawList in CrawlerNameModel.select_crwname(cra_nama, index):
                    print("crwawlist==={}".format(crawList))
                    scraper.homePage(start_digiket_url, proxy, crawList)
        except BaseException as e:
            print("Was a nice sleep, now let me continue...{}".format(e))
            time.sleep(5)
            continue
