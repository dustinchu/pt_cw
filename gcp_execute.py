from model.gcp_dbclass1 import DBClass1Model
from model.gcp_brand import BrandModel
from model.gcp_product import ProductModel
from model.gcp_product_additionalt import ProducAdditionaltModel
from model.gcp_product_sheet import ProducDatasheetModel
from model.gcp_product_qty_price import ProducQtyPriceModel
import json
import sys
import time
import re


# json_data = {"Stock": "1772", "Categories": "Capacitors Accessories", "Manufacturer": "Cornell Dubilier", "Series": "TH", "HomeName": "Capacitors", "PartNumber": "TH25", "DigiKeyPartNumber": "338-3603-ND", "Description": "ELECTRONIC MOUNTING CLIP HORIZ 1.375IN DIA ", "MetaDescription": "Cornell TH25 ELECTRONIC MOUNTING CLIP HORIZ 1.375IN DIA , data sheet, SPEC,drawing, inventory& pricing of electronic components ,from  Pingkai Technology CO.,LTD.", "KeyWords": "TH25 TH25 catalog TH25in stock TH25 pricing TH25 Cornell", "price": [{"PRICEBREAK": "1", "UNITPRICE": "120.280", "EXTENDEDPRICE": "120.28"}, {"PRICEBREAK": "10", "UNITPRICE": "116.690", "EXTENDEDPRICE": "1166.90"}, {"PRICEBREAK": "50", "UNITPRICE": "104.643", "EXTENDEDPRICE": "5232.18"}, {"PRICEBREAK": "100", "UNITPRICE": "91.228", "EXTENDEDPRICE": "9122.85"}, {"PRICEBREAK": "500", "UNITPRICE": "75.126", "EXTENDEDPRICE": "37563.25"}, {"PRICEBREAK": "1,000", "UNITPRICE": "69.761", "EXTENDEDPRICE": "69761.43"}, {"PRICEBREAK": "2,500", "UNITPRICE": "68.419", "EXTENDEDPRICE": "171048.83"}, {"PRICEBREAK": "5,000", "UNITPRICE": "67.078", "EXTENDEDPRICE": "335390.11"}], "Packaging": "Bulk", "Specifications": "-", "SeriesName": "-", "Category": "-", "Producttype": "-", "Ratedcurrent": "-", "Ratedvoltage": "-", "Mountingdirection": "-", "Catalog": "-", "Numberofpoles": "-", "NumberofPositions": "-", "NumberofRows": "-", "ConnectorType": "-", "MountingType": "-", "ConnectorStyle": "-", "Color": "-", "DielectricMaterial": "-", "RowSpacing": "-", "CableTermination": "-", "Style": "-", "MaterialFlammabilityRating": "-", "FlatFlexType": "-", "PowerWatts": "-", "TemperatureCoefficient": "-", "OperatingTemperature": "-", "Features": "-", "SizeDimension": "-", "ResistanceOhms": "-", "Type": "-", "LifetimeTemp": "-", "RippleCurrentLowFrequency": "-", "RippleCurrentHighFrequency": "-", "NumberofCapacitors": "-", "ThicknessMax": "-", "BasePartNumber": "-", "CapacitanceRange": "-", "CoilCurrent": "-", "CoilVoltage": "-", "ContactForm": "-", "ContactRatingCurrent":
#              "-", "SwitchingVoltage": "-", "MustOperateVoltage": "-", "OperateTime": "-", "ReleaseTime": "-", "TerminationStyle": "-", "ContactMaterial": "-", "CoilPower": "-", "CoilResistance": "-", "Circuit": "-", "OutputType": "-", "VoltageInput": "-", "VoltageLoad": "-", "LoadCurrent": "-", "OnStateResistanceMax": "-", "PackageCase": "-", "SupplierDevicePackage": "-", "CurrentInput": "-", "VoltageOutput": "-", "CurrentOutput": "-", "TurnOnTime": "-", "TurnOffTime": "-", "Pitch": "-", "ContactFinish": "-", "Resistance": "-", "MustReleaseVoltage": "-", "Tolerance": "-", "WireGauge": "-", "Capacitance": "-", "VoltageRated": "-", "datasheet": "[{'name': 'Capacitor Hardware, Mounting Options', 'url': 'http://www.cde.com/resources/catalogs/hardware.pdf'}]"}
# 找到大類的pkey 沒有資料的話要寫值 直接寫死
# result = DBClass1Model.dbclass1_find_by_str_name('Relays')
# print(result[0]['PKey'])

# str name = 品牌原本json 名稱Manufacturer  沒有資料寫值
def brand(json_data):
    result = BrandModel.brand_find_by_str_name(json_data['Manufacturer'])
    if result==[]:
        brand_json = {}
        brand_json['strName'] = json_data['Manufacturer']
        brand_model = BrandModel(**brand_json)
        brand_model.save_to_db()
#  判斷產品
def product(json_data):
    result = ProductModel.product_find_by_str_name(json_data['DigiKeyPartNumber'])
    if result ==[]:
        product_json = {}
        product_json['Description']=json_data['Description']
        product_json['Keywords']=json_data['KeyWords']
        product_json['DigiKeyPartNumber']=json_data['DigiKeyPartNumber']
        product_json['PartNumber']=json_data['PartNumber']
        product_json['Stock']=json_data['Stock']
        product_json['MetaDescription']=json_data['MetaDescription']
        product_json['Categories']=json_data['Categories']
        product_json['Manufacturer']=json_data['Manufacturer']
        product_json['Series']=json_data['Series']
        product_json['HomeName']=json_data['HomeName']
        product_model = ProductModel(**product_json)
        product_model.save_to_db()
        # print(result[0]['PKey'])
#datasheet
def datasheet(json_data):
    result = ProducDatasheetModel.product_find_by_str_name(json_data['DigiKeyPartNumber'])
    if result ==[]:
        datasheet_json ={}
        datasheet_json['DigiKeyPartNumber']=json_data['DigiKeyPartNumber']
        datasheet_json['datasheet']=str(json_data['datasheet'])

        datasheet_model = ProducDatasheetModel(**datasheet_json)
        datasheet_model.save_to_db()
    
def price(json_data):
    result = ProducQtyPriceModel.product_find_by_str_name(json_data['DigiKeyPartNumber'])
    if result ==[]:
        price_json ={}
        price_json['DigiKeyPartNumber']=json_data['DigiKeyPartNumber']
        price_json['price']=str(json_data['price'])
        price_model = ProducQtyPriceModel(**price_json)
        price_model.save_to_db()

def additionalt(json_data):
    result = ProducAdditionaltModel.product_find_by_str_name(json_data['DigiKeyPartNumber'])
    if result ==[]:
        additionalt_json ={}
        additionalt_json['DigiKeyPartNumber']=json_data['DigiKeyPartNumber']
        additionalt_json['additional']=str(json_data['body'])
        additionalt_model = ProducAdditionaltModel(**additionalt_json)
        additionalt_model.save_to_db()

def open_json(page_num):
    index =0
    with open(r'C:\品凱digikey\json\{}.json'.format(page_num), 'r') as openfile: 
        json_object = json.load(openfile) 
    for i  in json_object:
        if i['HomeName'] =='Relays':
            sp_count_arr = [m.start() for m in re.finditer('stock', i['KeyWords'])]
            for count in sp_count_arr:
                print(count)
                if count>0:
                    i['KeyWords'] =  i['KeyWords'].replace(',',' ')[:count+5]+','+ i['KeyWords'].replace(',',' ')[count+5:]
            # print(i)
            # break
        else:
            sp_count_arr = [m.start() for m in re.finditer(i['PartNumber'], i['KeyWords'])]
            for count in sp_count_arr:
                if count>0:
                    i['KeyWords'] =  i['KeyWords'][:count-1]+','+ i['KeyWords'][count:]
        if index ==100:
            break
        else:
            brand(i)
            product(i)
            datasheet(i)
            price(i)
            additionalt(i)
            index +=1
        # tStart = time.time() 
        # sql_json_arr={}
        # sql_json_arr['contents']=str(i)
        # crw_log_data = APILogModel(**sql_json_arr)
        # crw_log_data.save_to_db()
        # tEnd = time.time()  # 計時結束
        # print("product %f sec" % (tEnd - tStart))  # 會自動做近位

if __name__ == "__main__":
    open_json(1)
    # datasheet()
    # price()
    # additionalt()


