from model.Crawler_name import CrawlerNameModel
import pymysql
crwjson = [
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - ARINC',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - ARINC Inserts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - DIN 41612',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - Hard Metric, Standard',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Backplane Connectors - Specialized',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Banana and Tip Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Banana and Tip Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Banana and Tip Connectors - Binding Posts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Banana and Tip Connectors - Jacks, Plugs',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Barrel - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Barrel - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Barrel - Audio Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Barrel - Power Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Between Series Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Blade Type Power Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Blade Type Power Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Blade Type Power Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Blade Type Power Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Card Edge Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Card Edge Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '1',
        'listName': 'Card Edge Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Card Edge Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Fiber Optic Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Fiber Optic Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Fiber Optic Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Fiber Optic Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Assemblies',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Frames',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Housings, Hoods, Bases',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Heavy Duty Connectors - Inserts, Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Keystone - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Keystone - Faceplates, Frames',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Keystone - Inserts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'LGH Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Memory Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Memory Connectors - Inline Module Sockets',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Memory Connectors - PC Card Sockets',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Memory Connectors - PC Cards - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Jacks',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Jacks With Magnetics',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Plug Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Plugs',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Wiring Blocks',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Modular Connectors - Wiring Blocks - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Photovoltaic (Solar Panel) Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Photovoltaic (Solar Panel) Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Photovoltaic (Solar Panel) Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Pluggable Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Pluggable Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Power Entry Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Power Entry Connectors - Inlets, Outlets, Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Rectangular Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Rectangular Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName':
        'Rectangular Connectors - Arrays, Edge Type, Mezzanine (Board to Board)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '2',
        'listName': 'Rectangular Connectors - Board In, Direct Wire to Board',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Circular Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Circular Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Circular Connectors - Backshells and Cable Clamps',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Circular Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Circular Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Coaxial Connectors (RF)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Coaxial Connectors (RF) - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Coaxial Connectors (RF) - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Coaxial Connectors (RF) - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Coaxial Connectors (RF) - Terminators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Contacts - Leadframe',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Contacts - Multi Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'Contacts, Spring Loaded and Pressure',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Shaped Connectors - Centronics',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Accessories - Jackscrews',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Adapters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Backshells, Hoods',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'D-Sub, D-Shaped Connectors - Terminators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'FFC, FPC (Flat Flexible) Connectors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'FFC, FPC (Flat Flexible) Connectors - Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'FFC, FPC (Flat Flexible) Connectors - Contacts',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '3',
        'listName': 'FFC, FPC (Flat Flexible) Connectors - Housings',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '4',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '1',
        'ePage': '100',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '5',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '101',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '6',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '201',
        'ePage': '300',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '7',
        'listName':
        'Rectangular Connectors - Board Spacers, Stackers (Board to Board)',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '8',
        'listName': 'Rectangular Connectors - Headers, Male Pins',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '9',
        'listName':
        'Rectangular Connectors - Headers, Receptacles, Female Sockets',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Rectangular Connectors - Contacts',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Rectangular Connectors - Free Hanging, Panel Mount',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Rectangular Connectors - Headers, Specialty Pin',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Rectangular Connectors - Housings',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Rectangular Connectors - Spring Loaded',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Shunts, Jumpers',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Sockets for ICs, Transistors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Sockets for ICs, Transistors - Accessories',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Sockets for ICs, Transistors - Adapters',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Solid State Lighting Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Solid State Lighting Connectors - Accessories',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Solid State Lighting Connectors - Contacts',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Accessories',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Accessories - Jumpers',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Accessories - Marker Strips',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Accessories - Wire Ferrules',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Adapters',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Barrier Blocks',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Contacts',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '10',
        'listName': 'Terminal Blocks - Din Rail, Channel',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Headers, Plugs and Sockets',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Interface Modules',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Panel Mount',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Power Distribution',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Specialized',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Blocks - Wire to Board',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Junction Systems',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminal Strips and Turret Boards',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Accessories',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Adapters',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Barrel, Bullet Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Foil Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Housings, Boots',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Knife Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Magnetic Wire Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - PC Pin Receptacles, Socket Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - PC Pin, Single Post Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Quick Connects, Quick Disconnect Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Rectangular Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Ring Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Screw Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Solder Lug Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Spade Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Specialized Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Turret Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Wire Pin Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Wire Splice Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'Terminals - Wire to Board Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'USB, DVI, HDMI Connectors',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'USB, DVI, HDMI Connectors - Accessories',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '11',
        'listName': 'USB, DVI, HDMI Connectors - Adapters',
        'sPage': '1',
        'ePage': '400',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Resistors',
        'category': '1',
        'listName': 'Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Resistors',
        'category': '1',
        'listName': 'Chassis Mount Resistors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Resistors',
        'category': '1',
        'listName': 'Resistor Networks, Arrays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Resistors',
        'category': '1',
        'listName': 'Specialized Resistors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Resistors',
        'category': '2',
        'listName': 'Through Hole Resistors',
        'sPage': '1',
        'ePage': '100',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '3',
        'listName': 'Through Hole Resistors',
        'sPage': '101',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '4',
        'listName': 'Through Hole Resistors',
        'sPage': '201',
        'ePage': '300',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '5',
        'listName': 'Through Hole Resistors',
        'sPage': '301',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '2',
        'listName': 'Through Hole Resistors',
        'sPage': '1',
        'ePage': '100',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '3',
        'listName': 'Through Hole Resistors',
        'sPage': '101',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '4',
        'listName': 'Through Hole Resistors',
        'sPage': '201',
        'ePage': '300',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '5',
        'listName': 'Through Hole Resistors',
        'sPage': '301',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '6',
        'listName': 'Through Hole Resistors',
        'sPage': '401',
        'ePage': '500',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '7',
        'listName': 'Through Hole Resistors',
        'sPage': '501',
        'ePage': '600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '8',
        'listName': 'Through Hole Resistors',
        'sPage': '601',
        'ePage': '700',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '9',
        'listName': 'Through Hole Resistors',
        'sPage': '701',
        'ePage': '800',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '10',
        'listName': 'Through Hole Resistors',
        'sPage': '801',
        'ePage': '900',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '11',
        'listName': 'Through Hole Resistors',
        'sPage': '901',
        'ePage': '1100',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '12',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '13',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '201',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '14',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '401',
        'ePage': '600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '15',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '601',
        'ePage': '800',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '16',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '801',
        'ePage': '1000',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '17',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1001',
        'ePage': '1200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '18',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1201',
        'ePage': '1400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '19',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1401',
        'ePage': '1600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '20',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1601',
        'ePage': '1800',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '21',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '1801',
        'ePage': '2000',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '22',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '2001',
        'ePage': '2200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '23',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '2201',
        'ePage': '2400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Resistors',
        'category': '24',
        'listName': 'Chip Resistor - Surface Mount',
        'sPage': '2401',
        'ePage': '2600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Aluminum - Polymer Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Aluminum Electrolytic Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Capacitor Networks, Arrays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Electric Double Layer Capacitors (EDLC), Supercapacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Film Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Mica and PTFE Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Niobium Oxide Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Silicon Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Tantalum - Polymer Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Tantalum Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Thin Film Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '1',
        'listName': 'Trimmers, Variable Capacitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Capacitors',
        'category': '2',
        'listName': 'Ceramic Capacitors',
        'sPage': '1',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '3',
        'listName': 'Ceramic Capacitors',
        'sPage': '201',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '4',
        'listName': 'Ceramic Capacitors',
        'sPage': '401',
        'ePage': '600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '5',
        'listName': 'Ceramic Capacitors',
        'sPage': '601',
        'ePage': '800',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '6',
        'listName': 'Ceramic Capacitors',
        'sPage': '801',
        'ePage': '1000',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '7',
        'listName': 'Ceramic Capacitors',
        'sPage': '1001',
        'ePage': '1200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Capacitors',
        'category': '8',
        'listName': 'Ceramic Capacitors',
        'sPage': '1201',
        'ePage': '1500',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Accessories',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Automotive Relays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Contactors (Electromechanical)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Contactors (Solid State)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'High Frequency (RF) Relays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'I/O Relay Module Racks',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'I/O Relay Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Power Relays, Over 2 Amps',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Reed Relays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Relay Sockets',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Safety Relays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Signal Relays, Up to 2 Amps',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Relays',
        'category': '1',
        'listName': 'Solid State Relays',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '12',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '301',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '13',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '401',
        'ePage': '500',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '14',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '501',
        'ePage': '600',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '15',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '601',
        'ePage': '700',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '16',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '701',
        'ePage': '800',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '17',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '801',
        'ePage': '900',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '18',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '901',
        'ePage': '1000',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '19',
        'listName': 'Card Edge Connectors - Edgeboard Connectors',
        'sPage': '1001',
        'ePage': '1100',
        'pageStatus': 'Y'
    },
 
    {
        'crwName': 'Connectors, Interconnects',
        'category': '20',
        'listName': 'Circular Connectors',
        'sPage': '1',
        'ePage': '100',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '21',
        'listName': 'Circular Connectors',
        'sPage': '101',
        'ePage': '200',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '22',
        'listName': 'Circular Connectors',
        'sPage': '201',
        'ePage': '300',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Connectors, Interconnects',
        'category': '23',
        'listName': 'Circular Connectors',
        'sPage': '301',
        'ePage': '400',
        'pageStatus': 'Y'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Audio Special Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - Application Specific',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - Clock Buffers, Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName':
        'Clock/Timing - Clock Generators, PLLs, Frequency Synthesizers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - Delay Lines',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - IC Batteries',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - Programmable Timers and Oscillators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Clock/Timing - Real Time Clocks',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - ADCs/DACs - Special Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - Analog Front End (AFE)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - Analog to Digital Converters (ADC)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - Digital Potentiometers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - Digital to Analog Converters (DAC)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Data Acquisition - Touch Screen Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Embedded - CPLDs (Complex Programmable Logic Devices)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Embedded - DSP (Digital Signal Processors)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName': 'Embedded - FPGAs (Field Programmable Gate Array)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '1',
        'listName':
        'Embedded - FPGAs (Field Programmable Gate Array) with Microcontrollers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Embedded - Microcontrollers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Embedded - Microcontrollers - Application Specific',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Embedded - Microprocessors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Embedded - PLDs (Programmable Logic Device)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Embedded - System On Chip (SoC)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Interface - Analog Switches - Special Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName':
        'Interface - Analog Switches, Multiplexers, Demultiplexers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Interface - CODECs',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Interface - Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '2',
        'listName': 'Interface - Direct Digital Synthesis (DDS)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Drivers, Receivers, Transceivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Encoders, Decoders, Converters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Filters - Active',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - I/O Expanders',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Modems - ICs and Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Sensor and Detector Interfaces',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Sensor, Capacitive Touch',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Serializers, Deserializers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Signal Buffers, Repeaters, Splitters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Signal Terminators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Specialized',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Telecom',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName':
        'Interface - UARTs (Universal Asynchronous Receiver Transmitter)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Interface - Voice Record and Playback',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Amplifiers - Audio',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName':
        'Linear - Amplifiers - Instrumentation, OP Amps, Buffer Amps',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Amplifiers - Special Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Amplifiers - Video Amps and Modules',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Analog Multipliers, Dividers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Comparators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Linear - Video Processing',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Logic - Buffers, Drivers, Receivers, Transceivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Logic - Comparators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Logic - Counters, Dividers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Logic - FIFOs Memory',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '3',
        'listName': 'Logic - Flip Flops',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Gates and Inverters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName':
        'Logic - Gates and Inverters - Multi-Function, Configurable',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Latches',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Multivibrators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Parity Generators and Checkers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Shift Registers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Signal Switches, Multiplexers, Decoders',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Specialty Logic',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Translators, Level Shifters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Logic - Universal Bus Functions',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Memory',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Memory - Batteries',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Memory - Configuration Proms for FPGAs',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Memory - Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - AC DC Converters, Offline Switchers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Battery Chargers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Battery Management',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Current Regulation/Management',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Display Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Energy Metering',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Full, Half-Bridge Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Gate Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Hot Swap Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Laser Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - LED Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Lighting, Ballast Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Motor Drivers, Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - OR Controllers, Ideal Diodes',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - PFC (Power Factor Correction)',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Power Distribution Switches, Load Drivers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Power Management - Specialized',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Power Over Ethernet (PoE) Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Power Supply Controllers, Monitors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - RMS to DC Converters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Supervisors',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Thermal Management',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - V/F and F/V Converters',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Reference',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - DC DC Switching Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - DC DC Switching Regulators',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - Linear',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - Linear + Switching',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - Linear Regulator Controllers',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'PMIC - Voltage Regulators - Special Purpose',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
    {
        'crwName': 'Integrated Circuits (ICs)',
        'category': '4',
        'listName': 'Specialized ICs',
        'sPage': '1',
        'ePage': '1',
        'pageStatus': 'N'
    },
]

for a in crwjson:
    user = CrawlerNameModel(**a)
    user.save_to_db()
