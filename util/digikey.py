import json


class Digikey():
    def check_json_data(self, attibutes):
        if "SeriesName" not in attibutes:
            attibutes["SeriesName"] = "-"
        if "Category" not in attibutes:
            attibutes["Category"] = "-"
        if "Producttype" not in attibutes:
            attibutes["Producttype"] = "-"
        if "Ratedcurrent" not in attibutes:
            attibutes["Ratedcurrent"] = "-"
        if "Ratedvoltage" not in attibutes:
            attibutes["Ratedvoltage"] = "-"
        if "Mountingdirection" not in attibutes:
            attibutes["Mountingdirection"] = "-"
        if "Catalog" not in attibutes:
            attibutes["Catalog"] = "-"
        if "Numberofpoles" not in attibutes:
            attibutes["Numberofpoles"] = "-"
        if "Categories" not in attibutes:
            attibutes["Categories"] = "-"
        if "Manufacturer" not in attibutes:
            Manufacturer = "-"
        if "Series" not in attibutes:
            attibutes["Series"] = "-"
        if "Packaging" not in attibutes:
            attibutes["Packaging"] = "-"
        if "NumberofPositions" not in attibutes:
            attibutes["NumberofPositions"] = "-"
        if "NumberofRows" not in attibutes:
            attibutes["NumberofRows"] = "-"
        if "ConnectorType" not in attibutes:
            attibutes["ConnectorType"] = "-"
        if "MountingType" not in attibutes:
            attibutes["MountingType"] = "-"
        if "ConnectorStyle" not in attibutes:
            attibutes["ConnectorStyle"] = "-"
        if "Color" not in attibutes:
            attibutes["Color"] = "-"
        if "DielectricMaterial" not in attibutes:
            attibutes["DielectricMaterial"] = "-"
        if "RowSpacing" not in attibutes:
            attibutes["RowSpacing"] = "-"
        if "CableTermination" not in attibutes:
            attibutes["CableTermination"] = "-"
        if "Style" not in attibutes:
            attibutes["Style"] = "-"
        if "MaterialFlammabilityRating" not in attibutes:
            attibutes["MaterialFlammabilityRating"] = "-"
        if "FlatFlexType" not in attibutes:
            attibutes["FlatFlexType"] = "-"
        if "PowerWatts" not in attibutes:
            attibutes["PowerWatts"] = "-"
        if "TemperatureCoefficient" not in attibutes:
            attibutes["TemperatureCoefficient"] = "-"
        if "OperatingTemperature" not in attibutes:
            attibutes["OperatingTemperature"] = "-"
        if "Features" not in attibutes:
            attibutes["Features"] = "-"
        if "SizeDimension" not in attibutes:
            attibutes["SizeDimension"] = "-"
        if "ResistanceOhms" not in attibutes:
            attibutes["ResistanceOhms"] = "-"
        if "Specifications" not in attibutes:
            attibutes["Specifications"] = "-"
        if "Type" not in attibutes:
            attibutes["Type"] = "-"
        if "LifetimeTemp" not in attibutes:
            attibutes["LifetimeTemp"] = "-"
        if "RippleCurrentLowFrequency" not in attibutes:
            attibutes["RippleCurrentLowFrequency"] = "-"
        if "RippleCurrentHighFrequency" not in attibutes:
            attibutes["RippleCurrentHighFrequency"] = "-"
        if "NumberofCapacitors" not in attibutes:
            attibutes["NumberofCapacitors"] = "-"
        if "ThicknessMax" not in attibutes:
            attibutes["ThicknessMax"] = "-"
        if "BasePartNumber" not in attibutes:
            attibutes["BasePartNumber"] = "-"
        if "CapacitanceRange" not in attibutes:
            attibutes["CapacitanceRange"] = "-"
        if "CoilCurrent" not in attibutes:
            attibutes["CoilCurrent"] = "-"
        if "CoilVoltage" not in attibutes:
            attibutes["CoilVoltage"] = "-"
        if "ContactForm" not in attibutes:
            attibutes["ContactForm"] = "-"
        if "ContactRatingCurrent" not in attibutes:
            attibutes["ContactRatingCurrent"] = "-"
        if "SwitchingVoltage" not in attibutes:
            attibutes["SwitchingVoltage"] = "-"
        if "MustOperateVoltage" not in attibutes:
            attibutes["MustOperateVoltage"] = "-"
        if "OperateTime" not in attibutes:
            attibutes["OperateTime"] = "-"
        if "ReleaseTime" not in attibutes:
            attibutes["ReleaseTime"] = "-"
        if "TerminationStyle" not in attibutes:
            attibutes["TerminationStyle"] = "-"
        if "ContactMaterial" not in attibutes:
            attibutes["ContactMaterial"] = "-"
        if "CoilPower" not in attibutes:
            attibutes["CoilPower"] = "-"
        if "CoilResistance" not in attibutes:
            attibutes["CoilResistance"] = "-"
        if "Circuit" not in attibutes:
            attibutes["Circuit"] = "-"
        if "OutputType" not in attibutes:
            attibutes["OutputType"] = "-"
        if "VoltageInput" not in attibutes:
            attibutes["VoltageInput"] = "-"
        if "VoltageLoad" not in attibutes:
            attibutes["VoltageLoad"] = "-"
        if "LoadCurrent" not in attibutes:
            attibutes["LoadCurrent"] = "-"
        if "OnStateResistanceMax" not in attibutes:
            attibutes["OnStateResistanceMax"] = "-"
        if "PackageCase" not in attibutes:
            attibutes["PackageCase"] = "-"
        if "SupplierDevicePackage" not in attibutes:
            attibutes["SupplierDevicePackage"] = "-"
        if "CurrentInput" not in attibutes:
            attibutes["CurrentInput"] = "-"
        if "VoltageOutput" not in attibutes:
            attibutes["VoltageOutput"] = "-"
        if "CurrentOutput" not in attibutes:
            attibutes["CurrentOutput"] = "-"
        if "TurnOnTime" not in attibutes:
            attibutes["TurnOnTime"] = "-"
        if "TurnOffTime" not in attibutes:
            attibutes["TurnOffTime"] = "-"
        if "Pitch" not in attibutes:
            attibutes["Pitch"] = "-"
        if "ContactFinish" not in attibutes:
            attibutes["ContactFinish"] = "-"
        if "Resistance" not in attibutes:
            attibutes["Resistance"] = "-"
        if "MustReleaseVoltage" not in attibutes:
            attibutes["MustReleaseVoltage"] = "-"
        if "Tolerance" not in attibutes:
            attibutes["Tolerance"] = "-"
        if "WireGauge" not in attibutes:
            attibutes["WireGauge"] = "-"
        if "Capacitance" not in attibutes:
            attibutes["Capacitance"] = "-"
        if "VoltageRated" not in attibutes:
            attibutes["VoltageRated"] = "-"
        return attibutes

    def get_data_body(self, s):
        j = {}
        j['Categories'] = s['Categories']
        j['Manufacturer'] = s['Manufacturer']
        j['Series'] = s['Series']
        j['Stock'] = s['Stock']
        j['HomeName'] = s['HomeName']
        j['PartNumber'] = s['PartNumber']
        j['DigiKeyPartNumber'] = s['DigiKeyPartNumber']
        j['Description'] = s['Description']
        j['MetaDescription'] = s['MetaDescription']
        j['KeyWords'] = s['KeyWords']
        s.pop('Categories')
        s.pop('Manufacturer')
        s.pop('Series')
        s.pop('Stock')
        s.pop('HomeName')
        s.pop('PartNumber')
        s.pop('Description')
        s.pop('MetaDescription')
        s.pop('KeyWords')
        if 'datasheet' in s.keys():
            s.pop('datasheet')
        if 'price' in s.keys():
            s.pop('price')
        return j, s

    def get_two_float(self, f_str, n):
        f_str = str(f_str)
        a, b, c = f_str.partition('.')

        c = (c + "0" * n)[:n]
        return ".".join([a, c])

    def getManu(self, Manufacturer):
        manu = ""
        if "-" in Manufacturer:
            manu = Manufacturer[0:Manufacturer.find("-")]
        elif " " in Manufacturer:
            manu = Manufacturer[0:Manufacturer.find(" ")]
        else:
            manu = Manufacturer
        return manu

    def getManufacturer(self, Manufacturer):

        manu = ""
        if "-" in Manufacturer:
            manu = Manufacturer[0:Manufacturer.find("-")]
        elif " " in Manufacturer:
            manu = Manufacturer[0:Manufacturer.find(
                " ", Manufacturer.find(" ")+1)]
        else:
            manu = Manufacturer
        return manu

    def getKeyWord(self, homename, partNum, Manufacturer, Categories):
        manu = self.getManu(Manufacturer)
        keyWord = ""
        if homename == 'Resistors' or homename == 'Capacitors' or homename == 'Integrated Circuits (ICs)':
            keyWord = partNum + ","
            keyWord += ","+partNum + " catalog "
            keyWord += ","+partNum + " in stock "
            keyWord += ","+partNum + " pricing "
            keyWord += ","+partNum + " " + manu
            return keyWord
        elif homename == 'Connectors' or homename == 'Relays':
            chName = ""
            if homename == "Connectors":
                chName = "連接器"
            elif homename == "Relays":
                chName = "繼電器"
            keyWord = partNum + 'in stock'
            keyWord +=  ","+manu+" "
            keyWord +=  ","+Categories[0:Categories.find(" ")]+" "
            keyWord +=  ","+chName+" "
            return keyWord

    def getNewManufactyrer(self, Manufa):
        if Manufa == '3M':
            return '3M'
        if Manufa == 'Adafruit Industries LLC':
            return 'Adafruit '
        if Manufa == 'Adam Tec':
            return 'Adam'
        if Manufa == 'Adam Tech':
            return 'Adam'
        if Manufa == 'Adels-Contact':
            return 'Adels'
        if Manufa == 'Alpha Wire':
            return 'Alph'
        if Manufa == 'Altech Corporatio':
            return 'Altech'
        if Manufa == 'Altech Corporation':
            return 'Altech'
        if Manufa == 'Altran Magnetics, LLC':
            return 'Altran '
        if Manufa == 'American Electrical Inc.':
            return 'American Electrical Inc.'
        if Manufa == 'Amphenol Aerospace Operations':
            return 'Amphenol '
        if Manufa == 'Amphenol Alden Products Company':
            return 'Amphenol '
        if Manufa == 'Amphenol Anyte':
            return 'Amphenol '
        if Manufa == 'Amphenol Anytek':
            return 'Amphenol '
        if Manufa == 'Amphenol ICC':
            return 'Amphenol '
        if Manufa == 'Amphenol ICC (Commercial Products)':
            return 'Amphenol '
        if Manufa == 'Amphenol ICC (FCI)':
            return 'Amphenol '
        if Manufa == 'Amphenol Industrial':
            return 'Amphenol '
        if Manufa == 'Amphenol Industrial Operations':
            return 'Amphenol '
        if Manufa == 'Amphenol LTW':
            return 'Amphenol '
        if Manufa == 'Amphenol NEXUS Technologies':
            return 'Amphenol '
        if Manufa == 'Amphenol PC':
            return 'Amphenol '
        if Manufa == 'Amphenol PCD':
            return 'Amphenol '
        if Manufa == 'Amphenol Sine':
            return 'Amphenol '
        if Manufa == 'Amphenol Sine Systems Corp':
            return 'Amphenol '
        if Manufa == 'Amphenol SV Microwave':
            return 'Amphenol '
        if Manufa == ' Anderson Power Products, Inc. ':
            return 'Anderson'
        if Manufa == 'Aries Electronics ':
            return 'Aries'
        if Manufa == 'Assmann WSW ':
            return 'Assmann'
        if Manufa == 'Assmann WSW Components ':
            return 'Assmann'
        if Manufa == 'AVX Corporatio':
            return 'AVX'
        if Manufa == 'AVX Corporation':
            return 'AVX'
        if Manufa == 'Banner Engineering':
            return 'Banner'
        if Manufa == 'Banner Engineering Corporation':
            return 'Banner'
        if Manufa == 'Belden Inc.':
            return 'Belden'
        if Manufa == 'Bivar Inc':
            return 'Bivar'
        if Manufa == 'Bivar Inc.':
            return 'Bivar'
        if Manufa == ' Bourns Inc. ':
            return 'Bourns'
        if Manufa == 'Broadcom Limited':
            return 'Broadcom'
        if Manufa == 'Bud Industries':
            return 'Bud Industries'
        if Manufa == 'Bulgin':
            return 'Bulgin '
        if Manufa == 'CarlisleIT':
            return 'CarlisleIT'
        if Manufa == 'Carlo Gavazzi':
            return 'Carlo'
        if Manufa == 'Carlo Gavazzi Inc':
            return 'Carlo'
        if Manufa == 'CEL':
            return 'CEL'
        if Manufa == 'Chip Quik Inc.':
            return 'Chip Quik '
        if Manufa == 'Chogori Technologies Inc':
            return 'Chogori '
        if Manufa == 'Cinch Connectivity':
            return 'Cinch'
        if Manufa == 'Cinch Connectivity Solutions':
            return 'Cinch'
        if Manufa == 'Cinch Connectivity Solutions AIM-Cambridge':
            return 'Cinch'
        if Manufa == 'CIT Relay and Switch':
            return 'CIT Relay and Switch'
        if Manufa == 'CNC Tech':
            return 'CNC Tech'
        if Manufa == 'Comus International':
            return 'Comus International'
        if Manufa == 'Conec':
            return 'Conec'
        if Manufa == 'Conta':
            return 'Conta'
        if Manufa == 'Conta-Clip, Inc.':
            return 'Conta'
        if Manufa == 'Conxall/Switchcraft':
            return 'Conxall/Switchcraft'
        if Manufa == 'Cornell Dubilier':
            return 'Cornell'
        if Manufa == 'Cornell Dubilier Electronics (CDE)':
            return 'Cornell'
        if Manufa == 'Coto Technology':
            return 'Coto'
        if Manufa == 'Crouzet':
            return 'Crouzet'
        if Manufa == 'CTS Resistor Products':
            return 'CTS '
        if Manufa == 'CUI Device':
            return 'CUI'
        if Manufa == 'CUI Devices':
            return 'CUI'
        if Manufa == 'Curtis Industrie':
            return 'Curtis'
        if Manufa == 'Curtis Industries':
            return 'Curtis'
        if Manufa == 'Curtis Instruments Inc.':
            return 'Curtis'
        if Manufa == 'Cvilux USA':
            return 'Cvilux USA'
        if Manufa == 'CW Industries':
            return 'CW Industries'
        if Manufa == 'Cynergy 3':
            return 'Cynergy 3'
        if Manufa == 'Delta Electronics/Cyntec':
            return 'Delta Electronics/Cyntec'
        if Manufa == 'Desco':
            return 'Desco'
        if Manufa == 'Digi':
            return 'Digi'
        if Manufa == 'E-T-A':
            return 'E-T-A'
        if Manufa == 'Eaton':
            return 'Eaton'
        if Manufa == 'Eaton - Bussmann Electrical Division':
            return 'Eaton'
        if Manufa == 'Eaton - Electronics Division':
            return 'Eaton'
        if Manufa == 'EDAC Inc':
            return 'EDAC '
        if Manufa == 'EDAC Inc.':
            return 'EDAC '
        if Manufa == 'ERNI Electronics, Inc. ':
            return 'ERNI'
        if Manufa == 'Essentra Component':
            return 'Essentra'
        if Manufa == 'Essentra Components':
            return 'Essentra'
        if Manufa == 'Finder Relays,':
            return 'Finder Relays'
        if Manufa == 'Finder Relays, Inc.':
            return 'Finder Relays'
        if Manufa == 'GC Electronics':
            return 'GC Electronics'
        if Manufa == 'GCT':
            return 'GCT'
        if Manufa == 'Grayhill Inc.':
            return 'Grayhill Inc.'
        if Manufa == 'HARTING':
            return 'HARTING'
        if Manufa == 'Harwin Inc':
            return 'Harwin Inc.'
        if Manufa == 'Harwin Inc.':
            return 'Harwin Inc.'
        if Manufa == 'HellermannTyton':
            return 'HellermannTyton'
        if Manufa == 'Hirose Electric':
            return 'Hirose'
        if Manufa == 'Hirose Electric Co Ltd':
            return 'Hirose'
        if Manufa == 'Hirose Electric Co Ltd [CI]':
            return 'Hirose'
        if Manufa == 'Hirschmann':
            return 'Hirschmann'
        if Manufa == 'Honeywell Sensing and Productivity Solutions':
            return 'Honeywell '
        if Manufa == 'IDEC':
            return 'IDEC'
        if Manufa == 'ifm efector, inc.':
            return 'ifm efector, inc.'
        if Manufa == 'Industrial Fiber':
            return 'Industrial'
        if Manufa == 'Industrial Fiber Optics':
            return 'Industrial'
        if Manufa == 'Industrial Shields':
            return 'Industrial'
        if Manufa == 'Infineon Technologies':
            return 'Infineon '
        if Manufa == 'IO Audio Technologies':
            return 'IO Audio '
        if Manufa == 'Isocom Components 2004 LTD':
            return 'Isocom '
        if Manufa == 'ITT Cannon,':
            return 'ITT '
        if Manufa == 'ITT Cannon, LLC ':
            return 'ITT '
        if Manufa == 'IXYS Integrated Circuits Division':
            return 'IXYS '
        if Manufa == 'JAE Electronic':
            return 'JAE '
        if Manufa == 'JAE Electronics':
            return 'JAE '
        if Manufa == 'Johanson Dielectrics Inc.':
            return 'Johanson '
        if Manufa == 'Johanson Manufacturin':
            return 'Johanson '
        if Manufa == 'Johanson Manufacturing':
            return 'Johanson '
        if Manufa == 'Johanson Technology':
            return 'Johanson '
        if Manufa == 'Johanson Technology Inc.':
            return 'Johanson '
        if Manufa == 'JST Sales':
            return 'JST'
        if Manufa == 'JST Sales America Inc.':
            return 'JST'
        if Manufa == 'Kaga Electronics USA':
            return 'Kaga '
        if Manufa == 'KEMET':
            return 'KEMET'
        if Manufa == 'Keystone Electronics':
            return 'Keystone '
        if Manufa == 'Knowles Syfe ':
            return 'Knowles'
        if Manufa == 'Knowles Syfer':
            return 'Knowles'
        if Manufa == 'KOA Speer':
            return 'KOA'
        if Manufa == 'KOA Speer Electronics, Inc.':
            return 'KOA'
        if Manufa == 'Kycon, Inc':
            return 'Kycon'
        if Manufa == 'Kycon, Inc.':
            return 'Kycon'
        if Manufa == 'Kyocera International':
            return 'Kyocera '
        if Manufa == 'Kyocera International Inc. Electronic Components':
            return 'Kyocera '
        if Manufa == 'Laird Technologies EMI':
            return 'Laird'
        if Manufa == 'Leader Tech Inc.':
            return 'Leader'
        if Manufa == 'LEMO':
            return 'LEMO'
        if Manufa == 'Littelfuse Inc':
            return 'Littelfuse'
        if Manufa == 'Littelfuse Inc. ':
            return 'Littelfuse'
        if Manufa == 'Lumberg Automation':
            return 'Lumberg'
        if Manufa == 'MENDA/EasyBraid':
            return 'MENDA/EasyBraid'
        if Manufa == 'METZ CONNECT ':
            return 'METZ '
        if Manufa == 'METZ CONNECT USA Inc.':
            return 'METZ '
        if Manufa == 'Microsemi Corporation':
            return 'Microsemi'
        if Manufa == 'Mill':
            return 'Mill-Max'
        if Manufa == 'Mill-Max Manufacturing Corp':
            return 'Mill-Max'
        if Manufa == 'Molex':
            return 'Molex'
        if Manufa == 'Mueller Electric Co':
            return 'Mueller '
        if Manufa == 'Murata Electronics':
            return 'Murata'
        if Manufa == 'Murata Power Solutions Inc.':
            return 'Murata'
        if Manufa == 'NorComp Inc':
            return 'NorComp Inc.'
        if Manufa == 'NorComp Inc.':
            return 'NorComp Inc.'
        if Manufa == 'ODU':
            return 'ODU'
        if Manufa == 'Ohmite':
            return 'Ohmite'
        if Manufa == 'Omnetics':
            return 'Omnetics'
        if Manufa == 'Omron Automation':
            return 'Omron '
        if Manufa == 'Omron Automation and Safety':
            return 'Omron '
        if Manufa == 'Omron Electronics Inc':
            return 'Omron '
        if Manufa == 'Omron Electronics Inc-EMC Div':
            return 'Omron '
        if Manufa == 'ON Semiconductor':
            return 'ON '
        if Manufa == 'On Shore':
            return 'OST'
        if Manufa == 'On Shore Technology Inc.':
            return 'OST'
        if Manufa == 'Panasonic Electric':
            return 'Panasonic '
        if Manufa == 'Panasonic Electric Works':
            return 'Panasonic '
        if Manufa == 'Panasonic Electronic':
            return 'Panasonic '
        if Manufa == 'Panasonic Electronic Components':
            return 'Panasonic '
        if Manufa == 'Panasonic Industrial':
            return 'Panasonic '
        if Manufa == 'Panasonic Industrial Automation Sales':
            return 'Panasonic '
        if Manufa == 'Panduit Corp':
            return 'Panduit Corp'
        if Manufa == 'Parallax Inc.':
            return 'Parallax Inc.'
        if Manufa == 'Pepperl+Fuchs, Inc.':
            return 'Pepperl+Fuchs, Inc.'
        if Manufa == 'Phoenix Contac':
            return 'Phoenix'
        if Manufa == 'Phoenix Contact':
            return 'Phoenix'
        if Manufa == 'Pi Supply':
            return 'Pi Supply'
        if Manufa == 'Preci':
            return 'Preci'
        if Manufa == 'Preci-Dip':
            return 'Preci'
        if Manufa == 'Radiall USA, Inc.':
            return 'Radiall USA, Inc.'
        if Manufa == 'Red Lion Controls':
            return 'Red Lion Controls'
        if Manufa == 'Riedon':
            return 'Riedon'
        if Manufa == 'Rosenberger':
            return 'Rosenberger'
        if Manufa == 'Samsung Electro':
            return 'Samsung'
        if Manufa == 'Samsung Electro-Mechanics':
            return 'Samsung'
        if Manufa == 'Samtec Inc':
            return 'Samtec '
        if Manufa == 'Samtec Inc.':
            return 'Samtec '
        if Manufa == 'Schmartboard, Inc':
            return 'Schmartboard, Inc.'
        if Manufa == 'Schurter Inc.':
            return 'Schurter Inc.'
        if Manufa == 'SCS':
            return 'SCS'
        if Manufa == 'Sensata':
            return 'Sensata'
        if Manufa == 'Sensata-Crydom':
            return 'Sensata'
        if Manufa == 'Sharp Microelectronics':
            return 'SHARP'
        if Manufa == 'SHARP/Socle Technology':
            return 'SHARP/Socle '
        if Manufa == 'Singatron Enterprises Co Ltd':
            return 'Singatron'
        if Manufa == 'SOURIAU':
            return 'SOURIAU'
        if Manufa == 'SOURIAU-SUNBANK':
            return 'SOURIAU'
        if Manufa == 'SparkFun Electronics':
            return 'SparkFun'
        if Manufa == 'Stackpole Electronics':
            return 'Stackpole '
        if Manufa == 'Stackpole Electronics Inc':
            return 'Stackpole '
        if Manufa == 'Standex-Meder Electronics':
            return 'Standex-Meder'
        if Manufa == 'Stewart Connector':
            return 'Stewart'
        if Manufa == 'Sullins Connector':
            return 'Sullins '
        if Manufa == 'Sullins Connector Solutions':
            return 'Sullins '
        if Manufa == 'Susumu':
            return 'Susumu'
        if Manufa == 'Switchcraft Inc':
            return 'Switchcraft Inc.'
        if Manufa == 'Switchcraft Inc.':
            return 'Switchcraft Inc.'
        if Manufa == 'Taiyo Yude':
            return 'Taiyo'
        if Manufa == 'Taiyo Yuden':
            return 'Taiyo'
        if Manufa == 'TDK Corporatio':
            return 'TDK'
        if Manufa == 'TDK Corporation':
            return 'TDK'
        if Manufa == 'TDK Electronics':
            return 'TDK'
        if Manufa == 'TDK Electronics Inc.':
            return 'TDK'
        if Manufa == 'TE Application Tooling':
            return 'TE'
        if Manufa == 'TE Connectivity':
            return 'TE'
        if Manufa == 'TE Connectivity Aerospace, Defense and Marine':
            return 'TE'
        if Manufa == 'TE Connectivity AMP Connectors':
            return 'TE'
        if Manufa == 'TE Connectivity Deutsch Connectors':
            return 'TE'
        if Manufa == 'TE Connectivity Passive Product':
            return 'TE'
        if Manufa == 'TE Connectivity Potter & Brumfield Relays':
            return 'TE'
        if Manufa == 'TE Connectivity Raychem Cable Protection':
            return 'TE'
        if Manufa == 'TE Energy & Utilities':
            return 'TE'
        if Manufa == 'Tensility International Corp':
            return 'Tensility'
        if Manufa == 'Thomas Research Products':
            return 'Thomas Research Products'
        if Manufa == 'Toshiba Semiconductor and Storage':
            return 'Toshiba'
        if Manufa == 'TT Electronics/Optek Technology':
            return 'TT '
        if Manufa == 'Tusonix a Subsidiary of CTS Electronic Components':
            return 'CTS '
        if Manufa == 'United Chemi':
            return 'United Chemi'
        if Manufa == 'United Chemi-Con':
            return 'United Chemi'
        if Manufa == 'US Relays and Technology, Inc.':
            return 'US Relays and Technology, Inc.'
        if Manufa == 'Vishay Beyschlag/Draloric/BC':
            return 'Vishay'
        if Manufa == 'Vishay Beyschlag/Draloric/BC Components':
            return 'Vishay'
        if Manufa == 'Vishay Dal':
            return 'Vishay'
        if Manufa == 'Vishay Dale':
            return 'Vishay'
        if Manufa == 'Vishay Huntington':
            return 'Vishay'
        if Manufa == 'Vishay Huntington Electric Inc.':
            return 'Vishay'
        if Manufa == 'Vishay Semiconductor Opto Division':
            return 'Vishay'
        if Manufa == 'Vishay Sfernic':
            return 'Vishay'
        if Manufa == 'Vishay Sfernice':
            return 'Vishay'
        if Manufa == 'Vishay Spragu':
            return 'Vishay'
        if Manufa == 'Vishay Sprague':
            return 'Vishay'
        if Manufa == 'Vishay Vitramo':
            return 'Vishay'
        if Manufa == 'Vishay Vitramon':
            return 'Vishay'
        if Manufa == 'WAGO Corporation':
            return 'WAGO'
        if Manufa == 'Walsin Technology Corporation':
            return 'Walsin'
        if Manufa == 'Weidmüller':
            return 'Weidmüller'
        if Manufa == 'Würth Elektroni':
            return 'Würth'
        if Manufa == 'Würth Elektronik':
            return 'Würth'
        if Manufa == 'Yageo':
            return 'Yageo'
        return Manufa
