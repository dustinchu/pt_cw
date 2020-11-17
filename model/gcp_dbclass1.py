
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, DateTime

class DBClass1Model(db.Model):
    __tablename__ = "dbclass1"
    PKey = db.Column(db.Integer, primary_key=True)
    intLang = db.Column(db.Integer,default=1)
    Module_PKey = db.Column(db.Integer,default=4)
    Sort = db.Column(db.Integer,default=0)
    strName = db.Column(db.String(50),default='')
    Upload = db.Column(db.String(5),default='')
    UserID = db.Column(db.String(20),default='')
    dtUDate = db.Column(DateTime, default=datetime.datetime.utcnow)
    dtDate = db.Column(DateTime, default=datetime.datetime.utcnow)
    def __init__(self, intLang, Module_PKey, Sort, strName, Upload,UserID,dtUDate,dtDate):
        self.intLang = intLang
        self.Module_PKey = Module_PKey
        self.Sort = Sort
        self.strName = strName
        self.Upload = Upload
        self.UserID = UserID
        self.dtUDate = dtUDate
        self.dtDate = dtDate
    def json(self):
        return {
            'PKey':self.PKey,
            'intLang': self.intLang,
            'Module_PKey': self.Module_PKey,
            'Sort': self.Sort,
            'strName': self.strName,
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
        return DBClass1Model

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def dbclass1_find_by_str_name(strNamr):
        return list(map(lambda x: x.json(), db.session.query(DBClass1Model).filter_by(strName=strNamr)))



# CrawlerLogModel.create_db()
# CrawlerLogModel.select_crwlog(crwName='yyy')

# result = DBClass1Model.select_all()
# print(result)