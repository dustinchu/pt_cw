import json
import sys
import time
import pymysql
import re
from model.api_log_test import APILogModel
def post(page_num):
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
        tStart = time.time() 
        sql_json_arr={}
        sql_json_arr['contents']=str(i)
        crw_log_data = APILogModel(**sql_json_arr)
        crw_log_data.save_to_db()
        tEnd = time.time()  # 計時結束
        print("product %f sec" % (tEnd - tStart))  # 會自動做近位

if __name__ == '__main__': 

    # i = sys.argv[1]
    post(1)
    # i = {'Stock': '10332', 'Categories': 'Relays Accessories', 'Manufacturer': 'TE Connectivity', 'Series': 'SCHRACK', 'HomeName': 'Relays', 'PartNumber': 'RT28516', 'DigiKeyPartNumber': 'PB957-ND', 'Description': 'ELECTRONIC CLIP RETAINING METAL PCB ', 'MetaDescription': 'TE RT28516 ELECTRONIC CLIP RETAINING METAL PCB , data sheet, SPEC,drawing, inventory& pricing of electronic components ,from  Pingkai Technology CO.,LTD.', 'KeyWords': 'RT28516,in stockTE Relays 繼電器 ', 'price': "[{'PRICEBREAK': '1', 'UNITPRICE': '15.520', 'EXTENDEDPRICE': '15.52'}, {'PRICEBREAK': '10', 'UNITPRICE': '14.356', 'EXTENDEDPRICE': '143.56'}, {'PRICEBREAK': '25', 'UNITPRICE': '12.726', 'EXTENDEDPRICE': '318.15'}, {'PRICEBREAK': '50', 'UNITPRICE': '12.086', 'EXTENDEDPRICE': '604.31'}, {'PRICEBREAK': '100', 'UNITPRICE': '11.446', 'EXTENDEDPRICE': '1144.60'}, {'PRICEBREAK': '250', 'UNITPRICE': '10.173', 'EXTENDEDPRICE': '2543.34'}, {'PRICEBREAK': '500', 'UNITPRICE': '9.538', 'EXTENDEDPRICE': '4769.49'}, {'PRICEBREAK': '1,000', 'UNITPRICE': '8.902', 'EXTENDEDPRICE': '8902.66'}, {'PRICEBREAK': '5,000', 'UNITPRICE': '8.584', 'EXTENDEDPRICE': '42922.50'}]", 'Packaging': '-', 'Specifications': '-', 'SeriesName': '-', 'Category': '-', 'Producttype': '-', 'Ratedcurrent': '-', 'Ratedvoltage': '-', 'Mountingdirection': '-', 'Catalog': '-', 'Numberofpoles': '-', 'NumberofPositions': '-', 'NumberofRows': '-', 'ConnectorType': '-', 'MountingType': '-', 'ConnectorStyle': '-', 'Color': '-', 'DielectricMaterial': '-', 'RowSpacing': '-', 'CableTermination': '-', 'Style': '-', 'MaterialFlammabilityRating': '-', 'FlatFlexType': '-', 'PowerWatts': '-', 'TemperatureCoefficient': '-', 'OperatingTemperature': '-', 'Features': '-', 'SizeDimension': '-', 'ResistanceOhms': '-', 'Type': '-', 'LifetimeTemp': '-', 'RippleCurrentLowFrequency': '-', 'RippleCurrentHighFrequency': '-', 'NumberofCapacitors': '-', 'ThicknessMax': '-', 'BasePartNumber': 'RT314', 'CapacitanceRange': '-', 'CoilCurrent': '-', 'CoilVoltage': '-', 'ContactForm': '-', 'ContactRatingCurrent': '-', 'SwitchingVoltage': '-', 'MustOperateVoltage': '-', 'OperateTime': '-', 'ReleaseTime': '-', 'TerminationStyle': '-', 'ContactMaterial': '-', 'CoilPower': '-', 'CoilResistance': '-', 'Circuit': '-', 'OutputType': '-', 'VoltageInput': '-', 'VoltageLoad': '-', 'LoadCurrent': '-', 'OnStateResistanceMax': '-', 'PackageCase': '-', 'SupplierDevicePackage': '-', 'CurrentInput': '-', 'VoltageOutput': '-', 'CurrentOutput': '-', 'TurnOnTime': '-', 'TurnOffTime': '-', 'Pitch': '-', 'ContactFinish': '-', 'Resistance': '-', 'MustReleaseVoltage': '-', 'Tolerance': '-', 'WireGauge': '-', 'Capacitance': '-', 'VoltageRated': '-', 'datasheet': '[]'}
    # sp_count_arr = [m.start() for m in re.finditer('stock', i['KeyWords'])]
    # for count in sp_count_arr:
    #     print(count)
    # if count>0:
    #     i['KeyWords'] =  i['KeyWords'].replace(',',' ')[:count+5]+','+ i['KeyWords'].replace(',',' ')[count+5:]
    #     print(i['KeyWords'])
    # print(sp_count_arr)


