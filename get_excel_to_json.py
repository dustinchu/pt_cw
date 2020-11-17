import pandas
import json
import requests

# #讀取 excel to json
excel_data_fragment = pandas.read_excel('0804.xlsx')

json_str = excel_data_fragment.to_json(orient='records')
print(type(json_str))

# #將excel 存成json
with open('json\data.json', 'w') as outfile:
    outfile.write(json_str) 
# #讀取json file
with open('json\data.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 

id = 0
page_index =1
json_data =[]
for i in json_object:
    json_file = {}
    # json_file['ID']= i['ID']
    json_file['Stock']=i['Stock']
    json_file['Categories']= i['Categories']
    json_file['Manufacturer']= i['Manufacturer']
    json_file['Series']= i['Series']
    json_file['HomeName']= i['HomeName']
    json_file['PartNumber']= i['PartNumber']
    json_file['DigiKeyPartNumber']=i['DigiKeyPartNumber']
    json_file['Description']=i['Description']
    json_file['MetaDescription']= i['MetaDescription']
    json_file['KeyWords']= i['KeyWords']
    json_file['price']= i['price']
    json_file['body']= i['body']
    # json_file['Packaging']= i['Packaging']
    # json_file['Specifications']= i['Specifications']
    # json_file['SeriesName']= i['SeriesName']
    # json_file['Category']= i['Category']
    # json_file['Producttype']= i['Producttype']
    # json_file['Ratedcurrent']= i['Ratedcurrent']
    # json_file['Ratedvoltage']= i['Ratedvoltage']
    # json_file['Mountingdirection']= i['Mountingdirection']
    # json_file['Catalog']= i['Catalog']
    # json_file['Numberofpoles']= i['Numberofpoles']
    # json_file['NumberofPositions']=i['NumberofPositions']
    # json_file['NumberofRows']= i['NumberofRows']
    # json_file['ConnectorType']= i['ConnectorType']
    # json_file['MountingType']= i['MountingType']
    # json_file['ConnectorStyle']= i['ConnectorStyle']
    # json_file['Color']= i['Color']
    # json_file['DielectricMaterial']= i['DielectricMaterial']
    # json_file['RowSpacing']= i['RowSpacing']
    # json_file['CableTermination']= i['CableTermination']
    # json_file['Style']= i['Style']
    # json_file['MaterialFlammabilityRating']= i['MaterialFlammabilityRating']
    # json_file['FlatFlexType']= i['FlatFlexType']
    # json_file['PowerWatts']= i['PowerWatts']
    # json_file['TemperatureCoefficient']= i['TemperatureCoefficient']
    # json_file['OperatingTemperature']= i['OperatingTemperature']
    # json_file['Features']= i['Features']
    # json_file['SizeDimension']= i['SizeDimension']
    # json_file['ResistanceOhms']= i['ResistanceOhms']
    # json_file['Type']= i['Type']
    # json_file['LifetimeTemp']= i['LifetimeTemp']
    # json_file['RippleCurrentLowFrequency']= i['RippleCurrentLowFrequency']
    # json_file['RippleCurrentHighFrequency']= i['RippleCurrentHighFrequency']
    # json_file['NumberofCapacitors']= i['NumberofCapacitors']
    # json_file['ThicknessMax']= i['ThicknessMax']
    # json_file['BasePartNumber']= i['BasePartNumber']
    # json_file['CapacitanceRange']= i['CapacitanceRange']
    # json_file['CoilCurrent']= i['CoilCurrent']
    # json_file['CoilVoltage']= i['CoilVoltage']
    # json_file['ContactForm']= i['ContactForm']
    # json_file['ContactRatingCurrent']= i['ContactRatingCurrent']
    # json_file['SwitchingVoltage']= i['SwitchingVoltage']
    # json_file['MustOperateVoltage']= i['MustOperateVoltage']
    # json_file['OperateTime']= i['OperateTime']
    # json_file['ReleaseTime']= i['ReleaseTime']
    # json_file['TerminationStyle']= i['TerminationStyle']
    # json_file['ContactMaterial']= i['ContactMaterial']
    # json_file['CoilPower']= i['CoilPower']
    # json_file['CoilResistance']= i['CoilResistance']
    # json_file['Circuit']= i['Circuit']
    # json_file['OutputType']= i['OutputType']
    # json_file['VoltageInput']= i['VoltageInput']
    # json_file['VoltageLoad']= i['VoltageLoad']
    # json_file['LoadCurrent']= i['LoadCurrent']
    # json_file['OnStateResistanceMax']= i['OnStateResistanceMax']
    # json_file['PackageCase']= i['PackageCase']
    # json_file['SupplierDevicePackage']= i['SupplierDevicePackage']
    # json_file['CurrentInput']= i['CurrentInput']
    # json_file['VoltageOutput']= i['VoltageOutput']
    # json_file['CurrentOutput']= i['CurrentOutput']
    # json_file['TurnOnTime']= i['TurnOnTime']
    # json_file['TurnOffTime']= i['TurnOffTime']
    # json_file['Pitch']= i['Pitch']
    # json_file['ContactFinish']= i['ContactFinish']
    # json_file['Resistance']= i['Resistance']
    # json_file['MustReleaseVoltage']= i['MustReleaseVoltage']
    # json_file['Tolerance']= i['Tolerance']
    # json_file['WireGauge']= i['WireGauge']
    # json_file['Capacitance']= i['Capacitance']
    # json_file['VoltageRated']= i['VoltageRated']
    json_file['datasheet']= i['datasheet']
    # print(json_file)
    

    json_data.append(json_file)
    id+=1
    # 判斷每500比 寫入
    if id == 1000:
        print(type(json_data))
        with open('json\{}.json'.format(page_index), 'w') as outfile:
            json.dump(json_data,outfile)
            # outfile.write(json_data)
            json_data=[]
            id=0
            page_index+=1
        # print(i['ID'])
    # post 品大後台
    # url_contents = 'http://34.80.244.160/path_load.php'
    # post_status = requests.post(url_contents, json=json_data)
    # print(post_status)


