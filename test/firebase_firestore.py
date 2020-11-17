# from model.Crawler_runSec import CrawlerRunSecModel
from model.Crawler_data import CrawlerFirstModel
import pandas as pd
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


homeJson = CrawlerFirstModel.find_by_home('Connectors')
# print(homeJson)
read_json = []
index = 0
# initializations
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# print(homeJson[0]['body'])
for i in homeJson:
    i.pop("status")
    i.pop("id")
    print(i["DigiKeyPartNumber"])
    if i["DigiKeyPartNumber"] !="":
        #adding second data
        doc_ref = db.collection('product').document('item').collection('Connectors')
        doc_ref.add(i)
    index+=1
    # print(index)
    if index == 1000:
        break
