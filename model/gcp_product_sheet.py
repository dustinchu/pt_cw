
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func


class ProducDatasheetModel(db.Model):
    __tablename__ = "product_datasheet"
    PKey = db.Column(db.Integer, primary_key=True)
    DigiKeyPartNumber = db.Column(db.String(50), index=True)
    datasheet = db.Column(db.Text())
    dtDate = db.Column(
    DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self,  DigiKeyPartNumber, datasheet):
        self.DigiKeyPartNumber = DigiKeyPartNumber
        self.datasheet = datasheet

    def json(self):
        return {
            'PKey': self.PKey,
            'DigiKeyPartNumber': self.DigiKeyPartNumber,
            'datasheet': self.datasheet,
            'dtDate': self.dtDate,
     
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return ProducDatasheetModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def product_find_by_str_name(DigiKeyPartNumber):
        return list(map(lambda x: x.json(), db.session.query(ProducDatasheetModel).filter_by(DigiKeyPartNumber=DigiKeyPartNumber)))


ProducDatasheetModel.create_db()
# CrawlerLogModel.select_crwlog(crwName='yyy')

# result = DBClass1Model.select_all()
# print(result)
