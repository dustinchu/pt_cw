# from model.Crawler_runSec import CrawlerRunSecModel
from model.Crawler_data import CrawlerFirstModel
import pandas as pd
import json
# data = CrawlerFirstModel.find_by_name('RP28500')
# if data is None:
#     print(data)
# else:
#     print(data[0]['id'])
#     # print(data['Categories'])

homeJson = CrawlerFirstModel.find_by_home('Capacitors')
# print(homeJson)
read_json = []
# print(homeJson[0]['body'])
for i in homeJson:
    # print(i['body'])
    aa = json.loads(i['body'].replace("'", "\""))
    rowJson = {}
    rowJson['Categories'] = i['Categories']
    rowJson['Manufacturer'] = i['Manufacturer']
    rowJson['Series'] = i['Series']
    rowJson['HomeName'] = i['HomeName']
    rowJson['PartNumber'] = i['PartNumber']
    rowJson['Description'] = i['Description']
    rowJson['MetaDescription'] = i['MetaDescription']
    rowJson['KeyWords'] = i['KeyWords']
    rowJson['price'] = i['price']
    rowJson['Packaging'] = aa['Packaging']
    rowJson['Specifications'] = aa['Specifications']
    rowJson['SeriesName'] = aa['SeriesName']
    rowJson['Category'] = aa['Category']
    rowJson['Producttype'] = aa['Producttype']
    rowJson['Ratedcurrent'] = aa['Ratedcurrent']
    rowJson['Ratedvoltage'] = aa['Ratedvoltage']
    rowJson['Mountingdirection'] = aa['Mountingdirection']
    rowJson['Catalog'] = aa['Catalog']
    rowJson['Numberofpoles'] = aa['Numberofpoles']
    rowJson['NumberofPositions'] = aa['NumberofPositions']
    rowJson['NumberofRows'] = aa['NumberofRows']
    rowJson['ConnectorType'] = aa['ConnectorType']
    rowJson['MountingType'] = aa['MountingType']
    rowJson['ConnectorStyle'] = aa['ConnectorStyle']
    rowJson['Color'] = aa['Color']
    rowJson['DielectricMaterial'] = aa['DielectricMaterial']
    rowJson['RowSpacing'] = aa['RowSpacing']
    rowJson['CableTermination'] = aa['CableTermination']
    rowJson['Style'] = aa['Style']
    rowJson['MaterialFlammabilityRating'] = aa['MaterialFlammabilityRating']
    rowJson['FlatFlexType'] = aa['FlatFlexType']
    rowJson['PowerWatts'] = aa['PowerWatts']
    rowJson['TemperatureCoefficient'] = aa['TemperatureCoefficient']
    rowJson['OperatingTemperature'] = aa['OperatingTemperature']
    rowJson['Features'] = aa['Features']
    rowJson['SizeDimension'] = aa['SizeDimension']
    rowJson['ResistanceOhms'] = aa['ResistanceOhms']
    rowJson['Type'] = aa['Type']
    rowJson['LifetimeTemp'] = aa['LifetimeTemp']
    rowJson['RippleCurrentLowFrequency'] = aa['RippleCurrentLowFrequency']
    rowJson['RippleCurrentHighFrequency'] = aa['RippleCurrentHighFrequency']
    rowJson['NumberofCapacitors'] = aa['NumberofCapacitors']
    rowJson['ThicknessMax'] = aa['ThicknessMax']
    rowJson['BasePartNumber'] = aa['BasePartNumber']
    rowJson['CapacitanceRange'] = aa['CapacitanceRange']
    rowJson['CoilCurrent'] = aa['CoilCurrent']
    rowJson['CoilVoltage'] = aa['CoilVoltage']
    rowJson['ContactForm'] = aa['ContactForm']
    rowJson['ContactRatingCurrent'] = aa['ContactRatingCurrent']
    rowJson['SwitchingVoltage'] = aa['SwitchingVoltage']
    rowJson['MustOperateVoltage'] = aa['MustOperateVoltage']
    rowJson['OperateTime'] = aa['OperateTime']
    rowJson['ReleaseTime'] = aa['ReleaseTime']
    rowJson['TerminationStyle'] = aa['TerminationStyle']
    rowJson['ContactMaterial'] = aa['ContactMaterial']
    rowJson['CoilPower'] = aa['CoilPower']
    rowJson['CoilResistance'] = aa['CoilResistance']
    rowJson['Circuit'] = aa['Circuit']
    rowJson['OutputType'] = aa['OutputType']
    rowJson['VoltageInput'] = aa['VoltageInput']
    rowJson['VoltageLoad'] = aa['VoltageLoad']
    rowJson['LoadCurrent'] = aa['LoadCurrent']
    rowJson['OnStateResistanceMax'] = aa['OnStateResistanceMax']
    rowJson['PackageCase'] = aa['PackageCase']
    rowJson['SupplierDevicePackage'] = aa['SupplierDevicePackage']
    rowJson['CurrentInput'] = aa['CurrentInput']
    rowJson['VoltageOutput'] = aa['VoltageOutput']
    rowJson['CurrentOutput'] = aa['CurrentOutput']
    rowJson['TurnOnTime'] = aa['TurnOnTime']
    rowJson['TurnOffTime'] = aa['TurnOffTime']
    rowJson['Pitch'] = aa['Pitch']
    rowJson['ContactFinish'] = aa['ContactFinish']
    rowJson['Resistance'] = aa['Resistance']
    rowJson['MustReleaseVoltage'] = aa['MustReleaseVoltage']
    rowJson['Tolerance'] = aa['Tolerance']
    rowJson['WireGauge'] = aa['WireGauge']
    rowJson['Capacitance'] = aa['Capacitance']
    rowJson['VoltageRated'] = aa['VoltageRated']

    rowJson['datasheet'] = i['datasheet']
    rowJson['status'] = i['status']
    read_json.append(rowJson)
    # print(read_json)
    # break


df = pd.DataFrame(read_json)
df.to_excel('0804.xlsx', index=False)
# df_json = pd.read_json(read_json)
# df_json.to_excel('0804.xlsx', index=False)

# with open('test.json', 'w', encoding='utf-8') as f:
#     json.dump(read_json, f, ensure_ascii=False, indent=4, sort_keys=True)

# df_json = pd.read_json('test.json')
# df_json.to_excel('0804.xlsx', index=False)

# df_json = pd.read_json(read_json)
# df_json.to_excel("DATAFILE.xlsx")
# df.to_excel('excel_output.xls',na_rep=11,columns=['index'])
