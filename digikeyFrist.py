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
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.digikey.com/products/en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-fetch-dest': 'style',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
}
target_headers1 = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.digikey.com/products/en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_gcl_au=1.1.1630470618.1603957343; TS01c48c64=01460246b647d50ec718bcf3e0daff9b323e6c900ee9b8196ff1bf2bc4f0eb54e391f2b5b3ed1eb6489d9017e5894dc2ac83d8d363; TS0132ff3a=01460246b65fdaa3dbae26c6c054152a7314c1ca66177e76877eee85da560d11a1551918a6d130adcf248f7aa2480faab0ffcd8a1b; _evga_6ce7=36a28663b60fff93.; dkuhint=false; TS018ea5c6=01460246b69a4781df47647a57b17e7798328c170d065a0487440bc037b9e7f08863f3bfc60ff4b8c143f85b46af3f15ac21a03be3; _ga=GA1.2.1727094265.1603957604; _gid=GA1.2.130502340.1603957604; EG-U-ID=D2caac81b2-87a6-47aa-931c-a842815cd565; EG-S-ID=C645ccd26d-860b-48a9-b647-71c12952a546; csscxt=4056680970.20480.0000; QSI_SI_9nMMPDqA0H0NQxf_intercept=true; QSI_HistorySession=https%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2F20~1603957604506%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2Fcard-edge-connectors-edgeboard-connectors%2F303%3FFV%3D-8%257C791%26quantity%3D0%26ColumnSort%3D0%26page%3D311%26pageSize%3D500~1603957621059%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproduct-detail%2Fen%2Fedac-inc%2F333-062-500-203%2F151-333-062-500-203-ND%2F10896386~1603957629145%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproducts%2Fen%2Fconnectors-interconnects%2Fcard-edge-connectors-edgeboard-connectors%2F303%3FFV%3D-8%257C791%26quantity%3D0%26ColumnSort%3D0%26page%3D311%26pageSize%3D500~1603957654621%7Chttps%3A%2F%2Fwww.digikey.tw%2Fproduct-detail%2Fen%2Fedac-inc%2F333-062-500-203%2F151-333-062-500-203-ND%2F10896386~1603957675851; ps-eudo-sid=%7b%22CustomerId%22%3a0%2c%22CustomerClass%22%3a0%2c%22Currency%22%3a%22USD%22%2c%22OrderModel%22%3a-1%7d; sid=168885019499253370xJWT1ZQ5D0F7T9CHAR7ZJEPAEY1EERD4HYANBC7OW054H5P8VMCUN7T76450HV77O; TS017613a9=01460246b69eaa7af6351d540d029294df51865a23f075e0ba3285d0d59e83e4bb66d52fe5ce7f6131961a47ef0397a686d5e4b0d1; TS018060f7=01460246b6f26b0bbd7b15d455c9bbedf467266321c6a43e61566016c953358cdf6c9372c1229de3afd32a10f0ebd0aca73793e0d0; bm_sz=9FE9CB32197ABD28C6BA6973A76C97B5~YAAQvIpFy5eTCXd1AQAAhgA6eAnpRPySMP7Sz0ep6EcAZY7dFeTPDlwbBkGgTvHmEDBuErpu/M2LJkgVWaJKv8frs/GeLXPcK8M4+MqglLaZdzMrORvcBFA/ncqpJxzWvq3SC2AhCZDfHOWNbbJtq8zSqG0LTKWROu1Zugkfsd1iSusp9sI2g2C/xK5Z0MwB; TS01d5128f=01460246b6d30edacb16356c5ac1406c81123b87e37925480ea6e220a534de842b3970e1765c799fde0e1d46584cf197b8be4ba807; RT="z=1&dm=digikey.tw&si=k54rpjsrpxb&ss=kguiu6r3&sl=0&tt=0"; utag_main=_sn:3$_ss:1$_st:1604041666924$v_id:01757352bc5e0022a1f1bd24999c03072003e06a00bd0$ses_id:1604039866924%3Bexp-session$_pn:1%3Bexp-session; _cs_mk=0.5826846981068476_1604039866978; TS013c3a0b=01460246b6cab4d89a039ba9e9c7d43cfe338c14d5ae5a36dca18ee551db8637e91b3b3c4db32d37c1902c3a8985096cba3c1569d4; _uetsid=542eac00198d11eba6d937612098a0e4; _uetvid=ddc9f92d9fa9b4deaf4ae7c82132c790; _gat_Production=1; ak_bmsc=1858A7197A365BAE6316FF5809D29B48CB458ABC300E0000BCB49B5F55F5DE58~plo5ueXcwfVRehIVwKC+RNDjsDWU5mrHFxIlAeXxUTH5Sd9Mb6wbXsWWjTYNtfEcL8VruWKEmP2hv+Kn7kdJkkfOzscUp9ka/0tWGsn8yQya7B31s6BwhQgDWTjBkntDtrbTmSaX9euIXwdRxb3QNvedifCNUkWtSmFUtmZyQDmXV1IC/IT4/ZRSuP4vUSoj6Fmf50y0xk1/qbsXwVXVaazb+t1axp+LRSD/3Ade3EzD0x7Svq+mr2lNQYATy4diex; bm_sv=9FDB5B461387DA5754D37A65CC5980C1~CDfZlYJQYfYO0ebeRfDkE9EVVrqZchgo2TtnL+UFyTmKcBt+Mo4oSk4ixiFdiVZWDT6Qo9fbsCwLD88sVtayWyYs0Q6CZE9AfEKe0OLo/rtfYtIL6HrvY4xwXoBz96dl2o2KaUMjAyjYd6jRXlpvNdYjZ/99+GmNPdQPWgeR5g0=; _abck=D50FA7FA01D42357BF6CA51E43D3C08C~0~YAAQvIpFy0CUCXd1AQAAJTM6eAT686psj5rXeKGq7OYPbetzNoYEew4TA/Hd44JIZKX5AhgLBadp1jL0NGJgKM0Rv1gFVpV58zA/tWI6HXlbUi+t8nzLdjG+tYlJ3UZVxGpXtx+OKbS+FvrfUGWbPTCmhoMVt0CGXFOOsFsw0gCwYRiLXMuJwJmVLrZAkmAp4Q8DzrHfxmnhqy6Hn0oia/tmQbTpxvUdkT4peMlkRCS2gIv/9YDkQxe8nq5FxDt0/7X21gNgO5KagzZOfLNxQuN8WC5AQrITknx+6LSEEXtYNnZ1quPhRzWUsRfPW/CABFmydfIKew==~-1~-1~-1',
    'sec-fetch-dest': 'style',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
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
                    print("看一下home==={} ".format(home_name))
                    self.homeIndexList(homedata=home,
                                       proxy=proxy,
                                       crw_list=crw_list)
            # break
        else:
            print("網址失效", home_url)

    # ?FV=-8%7C1010&quantity=0&ColumnSort=0&page=1&pageSize=500

    def homeIndexList(self, homedata, proxy, crw_list):
        count_index = 1
        # crw_start_name = crw_list['listName']
        
        print("url==={}".format(homedata["home_url"]))
        body_r = requests.get(url=homedata["home_url"],
                              headers=target_headers,
                              proxies=proxy)
        body_doc = PyQuery(body_r.text)
        if body_r.status_code == 200:
            for body_list in body_doc('.catfiltersub > li').items():
                body_url = "https://www.digikey.tw" + body_list(
                    'a').attr['href']
                print("body_url==={}".format(body_url))
                body_name = body_list('a').text()

                crw_list_name = CrawlerOnlineModel.select_crwOnline(
                    crwTitle=crw_list['crwName'], index=crw_list['category'])
                # 沒資料將第一筆寫入
                if crw_list_name == []:
                    online_json = {}
                    online_json['crwTitle'] = crw_list['crwName']
                    online_json['crwName'] = crw_list['listName']
                    online_json['partNum'] = 'frist'
                    online_json['DigiKeyPartNumber'] = 'frist'
                    online_json['page'] = crw_list['sPage']
                    online_json['onlineIndex'] = crw_list['category']
                    onlineModel = CrawlerOnlineModel(**online_json)
                    onlineModel.save_to_db()
                # else:
                #     if crw_start_name == crw_list_name[0]['crwName']:
                #         crw_start_name = crw_list_name[0]['crwName']
                #     else:
                #         CrawlerOnlineModel.update_crwOnline(
                #             crwTitle=crw_list['crwName'],
                #             crwName=crw_list['listName'],
                #             page=crw_list['sPage'],
                #             partNum='frist',
                #             DigiKeyPartNumber = 'frist',
                #             index=crw_list['category'])

                if crw_list_name[0]['crwName'] == body_name:
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
        pageStatus = False
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
            if pageStatus:
                crw_page = int(sPageCount) + i -1
            else:
                crw_page = int(sPageCount) + i
            body_url = indexList[
                'indexListUrl'] + "?FV=-8%7C791&quantity=0&ColumnSort=0&page={pageno}&pageSize=500"
            
            body_url = body_url.format(pageno=crw_page)
            print("body_url====={}".format(body_url))
            data_r = requests.get(url=body_url,
                                  headers=target_headers,
                                  proxies=proxy)
            # data_r = requests.get(url=body_url, headers=headers)
            if data_r.status_code == 200:
                productDoc = PyQuery(data_r.text)
                itemno =1
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
                                    print("partNum===:{}".format(partNum))
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
                                        # DigiKetPartNum
                                        productListData["DigiKeyPartNumber"] = trs[3].text(
                                        ).strip()
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
                                        print("product Url:\n{}".format(productListData["productUrl"]))
                                        break
                        else:
                            # 前兩筆會是null 第三筆還是null 跳出
                            if (itemno == 3):
                                break
                        itemno += 1

                # 沒資料 代表這頁沒東西 直接跳出 換下一個listname 撈取
                else:
                    # 找到現在的的listname index+1 update
                    crw_name_json = CrawlerNameModel.select_crwname(
                        crwName=crw_list['crwName'],
                        category=crw_list['category'])
                    json_name_index = 0
                    for json_name in crw_name_json:
                        json_name_index += 1
                        if json_name["listName"] == crw_list_name[0]['crwName']:
                            print("看一下json index{}".format(json_name_index))
                            break
                    
                    try:
                        print("下一個list 資料{}".format(crw_name_json[json_name_index]))
                        print(crw_list['crwName'],crw_name_json[json_name_index]['listName'],crw_list['category'])
                        CrawlerOnlineModel.update_crwOnline(
                            crwTitle=crw_list['crwName'],
                            crwName=crw_name_json[json_name_index]['listName'],
                            page='1',
                            partNum='frist',
                            DigiKeyPartNumber='frist',
                            index=crw_list['category'])
                    except:
                        CrawlerOnlineModel.delete_crwOnline(
                            crwTitle=crw_list['crwName'],
                            index=crw_list['category'])
                    break
            else:
                print("網址失效~!=200")
            # 如果crwStatus = True 代表有找到上次爬的位置 初始頁面page+i
            if  crwStatus:
                pageStatus = False
            else:
                #沒找到的話 就從上一頁開始 
                pageStatus = True            
                crwStatus = True
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
        # urlencode = productItemData["DigiKeyPartNumber"].replace("!", "%21").replace("\"", "%22").replace("#", "%23").replace("$", "%24").replace("%", "%25").replace(")", "%29").replace("&", "%26").replace("'", "%27").replace("(", "%28").replace("*", "%2a").replace("+", "%2b").replace(",", "%2c").replace(".", "%2e").replace("/", "%2f")
        print("product Url:\n{}".format(productItemData["productUrl"]))
        # print("url=={}".format("https://www.digikey.com/products/en?keywords={}".format(urlencode)))
        r = requests.get(url=productItemData["productUrl"],
                         headers=target_headers1,
                         proxies=proxy)
        with open('we2bpage.html', 'w', encoding="utf-8") as f:
            f.write(r.text)
        # r = requests.get(url="https://www.digikey.com/products/en?keywords={}".format(urlencode),
        #             headers=target_headers,
        #             proxies=proxy)
        # r = requests.get(url=productItemData["productUrl"])
        # print("DOC===")
        doc = PyQuery(r.text)
        # print(doc)
        attibutes = {}
        prices_qty_data = []
        datasheet_data = []

        
        for product_overview in doc('table[id=product-overview]').items():
            for product_tbody in product_overview('tr').items():
                if product_tbody('th').text() == 'Description':
                    productItemData["Description"] = product_tbody(
                        'td').text().replace("Copy", "").replace("\n", "")
        if doc('.product-details-procurement > .product-details-headline').text() != 'Non-Stock':
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
                                print(e)
                                # send_line.lineNotifyMessage(
                                #     "{}\nBaseException!! \n{}".format(productItemData["productUrl"], e))
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
            attibutes["DigiKeyPartNumber"] = productItemData["DigiKeyPartNumber"]
            attibutes["PartNumber"] = productItemData["PartNumber"]
            attibutes[
                "Description"] = "ELECTRONIC " + productItemData["Description"]
            attibutes["MetaDescription"] = "-"
            attibutes["Manufacturer"] = digikey_uril.getNewManufactyrer(Manufa=attibutes["Manufacturer"])
            menu = digikey_uril.getManu(Manufacturer=attibutes["Manufacturer"])

            attibutes["Manufacturer"] = digikey_uril.getManufacturer(
                Manufacturer=attibutes["Manufacturer"])

            attibutes["MetaDescription"] = menu + " " + productItemData[
                "PartNumber"] + " " + attibutes[
                    "Description"] + ", data sheet, SPEC,drawing, inventory& pricing of electronic components ,from  Pingkai Technology CO.,LTD."

            attibutes["KeyWords"] = digikey_uril.getKeyWord(
                homename=attibutes["HomeName"],
                partNum=productItemData["PartNumber"],
                Manufacturer=attibutes["Manufacturer"],
                Categories=attibutes['Categories'])

            print("att json ====".format(attibutes))

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
            print(json_data)
            # print("-----------------------------------------------")
            # url_contents = 'http://demo5.tsg.com.tw/19/p-team/path_load.php'

            tStart = time.time()  # 計時開始

            # data = CrawlerFirstModel.find_by_name(
            #     PartNumber=attibutes["PartNumber"], DigiKeyPartNumber=attibutes["DigiKeyPartNumber"])
            # j, s = digikey_uril.get_data_body(
            #     digikey_uril.check_json_data(attibutes))
            # sql_json_arr = j
            # sql_json_arr["body"] = str(s)
            # sql_json_arr["price"] = str(prices_qty_data)
            # sql_json_arr["datasheet"] = str(datasheet_data)

            # # print("SQL====\n{}".format(sql_json_arr))
            # if doc('.product-details-procurement > .product-details-headline').text() != 'Non-Stock':
            #     sql_json_arr['status'] = "NULL"
            # else:
            #     sql_json_arr['status'] = "non-Stock"
            # if data == []:
            #     crw_log_data = CrawlerFirstModel(**sql_json_arr)
            #     crw_log_data.save_to_db()
            # else:
            #     print("update==={}".format(CrawlerFirstModel.update_to_db(
            #         id=data[0]['id'], sql_json_arr=sql_json_arr)))
            # print("part=={}".format(productItemData["PartNumber"]))
            CrawlerOnlineModel.update_crwOnline(
                crwTitle=productItemData['homeName'],
                crwName=productItemData['indexListName'],
                page=crw_page,
                partNum=productItemData["PartNumber"],
                DigiKeyPartNumber=productItemData["DigiKeyPartNumber"],
                index=crw_list['category'])

            # 計時結束
            tEnd = time.time()
            post_sec = tEnd - tStart
            print("inset update %f sec" % (tEnd - tStart))  # 會自動做近位


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
        # try:
        proxy = proxy_msg.getConnectProxy()
        print(proxy)
        html = requests.get('https://www.digikey.tw/products/en',
                            proxies=proxy,
                            headers=target_headers)
        if html.status_code == 200:

            for crawList in CrawlerNameModel.select_crwname(cra_nama, index):
                print("crwawlist==={}".format(crawList))
                scraper.homePage(start_digiket_url, proxy, crawList)
        # except BaseException as e:
        #     print("Was a nice sleep, now let me continue...{}".format(e))
        #     time.sleep(2)
        #     continue
