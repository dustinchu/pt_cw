
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func


class BrandModel(db.Model):
    __tablename__ = "product_brand"
    PKey = db.Column(db.Integer, primary_key=True)
    intLang = db.Column(db.Integer, default=1)
    Module_PKey = db.Column(db.Integer, default=4)
    Sort = db.Column(db.Integer, default=0)
    strName = db.Column(db.String(100), default='')
    Contents = db.Column(db.Text())
    Upload = db.Column(db.String(5), default='Yes')
    UserID = db.Column(db.String(20), default='Admin')
    dtUDate = db.Column(
        DateTime, server_default=func.now(), onupdate=func.now())
    dtDate = db.Column(
        DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self,  strName,):
        # self.intLang = intLang
        # self.Module_PKey = Module_PKey
        # self.Sort = Sort
        self.strName = strName
        # self.Contents = Contents
        # self.Upload = Upload
        # self.UserID = UserID

    def json(self):
        return {
            'PKey': self.PKey,
            'intLang': self.intLang,
            'Module_PKey': self.Module_PKey,
            'Sort': self.Sort,
            'strName': self.strName,
            'Contents': self.Contents,
            'Upload': self.Upload,
            'UserID': self.UserID,
            'dtUDate': self.dtUDate,
            'dtDate': self.dtDate,
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return BrandModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def brand_find_by_str_name(strNamr):
        return list(map(lambda x: x.json(), db.session.query(BrandModel).filter_by(strName=strNamr)))


BrandModel.create_db()
# CrawlerLogModel.select_crwlog(crwName='yyy')

# result = DBClass1Model.select_all()
# print(result)
