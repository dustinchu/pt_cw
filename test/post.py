import requests
body = [{
    "id":
    1,
    "HomeName":
    "Relays",
    "count":
    1,
    "indexListName":
    "Accessories",
    "PartNumber":
    "HS072",
    "Description":
    "ELECTRONIC HEATSINK SSR 0.7DEG C/W PNL MNT",
    "ProductUrl":
    "https://www.digikey.tw/product-detail/en/sensata-crydom/HS072/CC1702-ND/2122811",
    "PageIndex":
    1,
    "KeyWords":
    "HS072, HS072 catalog, HS072 in stock, HS072 pricing, HS072 Sensata-Crydom Copy",
    "Categories":
    "Relays Accessories",
    "Manufacturer":
    "Sensata-Crydom",
    "Series":
    "HS",
    "Packaging":
    "-",
    "NumberofPositions":
    "-",
    "NumberofRows":
    "-",
    "ConnectorType":
    "-",
    "MountingType":
    "-",
    "ConnectorStyle":
    "-",
    "Color":
    "-",
    "DielectricMaterial":
    "-",
    "RowSpacing":
    "-",
    "CableTermination":
    "-",
    "Style":
    "-",
    "MaterialFlammabilityRating":
    "-",
    "FlatFlexType":
    "-",
    "PowerWatts":
    "-",
    "TemperatureCoefficient":
    "-",
    "OperatingTemperature":
    "-",
    "SizeDimension":
    "-",
    "ResistanceOhms":
    "-",
    "Specifications":
    "-",
    "Type":
    "-",
    "LifetimeTemp":
    "-",
    "RippleCurrentLowFrequency":
    "-",
    "RippleCurrentHighFrequency":
    "-",
    "NumberofCapacitors":
    "-",
    "ThicknessMax":
    "-",
    "BasePartNumber":
    "-",
    "CapacitanceRange":
    "-",
    "CoilCurrent":
    "-",
    "CoilVoltage":
    "-",
    "ContactForm":
    "-",
    "ContactRatingCurrent":
    "-",
    "SwitchingVoltage":
    "-",
    "MustOperateVoltage":
    "-",
    "OperateTime":
    "-",
    "ReleaseTime":
    "-",
    "TerminationStyle":
    "-",
    "ContactMaterial":
    "-",
    "CoilPower":
    "-",
    "CoilResistance":
    "-",
    "Circuit":
    "-",
    "OutputType":
    "-",
    "VoltageInput":
    "-",
    "VoltageLoad":
    "-",
    "LoadCurrent":
    "-",
    "OnStateResistanceMax":
    "-",
    "PackageCase":
    "-",
    "SupplierDevicePackage":
    "-",
    "CurrentInput":
    "-",
    "VoltageOutput":
    "-",
    "CurrentOutput":
    "-",
    "TurnOnTime":
    "-",
    "TurnOffTime":
    "-",
    "Pitch":
    "-",
    "ContactFinish":
    "-",
    "Resistance":
    "-",
    "MustReleaseVoltage":
    "-",
    "Tolerance":
    "-",
    "WireGauge":
    "-",
    "Capacitance":
    "-",
    "VoltageRated":
    "-",
    "SeriesName":
    "-",
    "Category":
    "-",
    "Producttype":
    "-",
    "Ratedcurrent":
    "-",
    "Ratedvoltage":
    "-",
    "Mountingdirection":
    "-",
    "Features":
    "-",
    "Numberofpoles":
    "-",
    "Catalog":
    "-",
 
   
}]
import json
# url_contents = 'http://192.168.161.61:5000/api/content'
url_contents = 'http://develop3.tsg.com.tw/19/p-team/03/path_load.php'
contents = requests.post(url_contents, json=body)
print(contents.text[10:len(contents.text)-1])
# post_status = json.loads(contents.text)
# print(post_status)
# print(type(post_status))