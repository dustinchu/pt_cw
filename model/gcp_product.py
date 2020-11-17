
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func

class ProductModel(db.Model):
    __tablename__ = "product_new"
    PKey = db.Column(db.Integer, primary_key=True)

    Description = db.Column(db.String(500), default='')
    Keywords = db.Column(db.String(500), default='')
    DigiKeyPartNumber = db.Column(db.String(50), nullable=False, index=True)
    PartNumber = db.Column(db.String(50), nullable=False, index=True)
    Stock = db.Column(db.Integer)
    MetaDescription = db.Column(db.String(200), default='')
    Categories = db.Column(db.String(50), default='', index=True)
    Manufacturer = db.Column(db.String(50), default='')
    Series = db.Column(db.String(50))
    HomeName = db.Column(db.String(50), default='', index=True)
    intLang = db.Column(db.Integer, default=1)
    Module_PKey = db.Column(db.Integer, default=0)
    Sort = db.Column(db.Integer, default=0)
    Interview = db.Column(db.String(255), default='')
    Upload = db.Column(db.String(5), default='Yes')
    UserID = db.Column(db.String(20), default='Admiin')
    dtUDate = db.Column(
    DateTime, server_default=func.now(), onupdate=func.now())
    dtDate =  db.Column(db.DateTime, default=func.now())

    def __init__(self, Description, Keywords, DigiKeyPartNumber, PartNumber, Stock, MetaDescription, Categories, Manufacturer, Series,HomeName):
        self.Description = Description
        self.Keywords = Keywords
        self.DigiKeyPartNumber = DigiKeyPartNumber
        self.PartNumber = PartNumber
        self.Stock = Stock
        self.MetaDescription = MetaDescription
        self.Categories = Categories
        self.Manufacturer = Manufacturer
        self.Series = Series
        self.HomeName = HomeName

    def json(self):
        return {
            'PKey': self.PKey,
            'Description': self.Description,
            'Keywords': self.Keywords,
            'DigiKeyPartNumber': self.DigiKeyPartNumber,
            'PartNumber': self.PartNumber,
            'Stock': self.Stock,
            'MetaDescription': self.MetaDescription,
            'Categories': self.Categories,
            'Manufacturer': self.Manufacturer,
            'Series':self.Series,
            'HomeName':self.HomeName,
            'intLang':self.intLang,
            'Module_PKey':self.Module_PKey,
            'Sort':self.Sort,
            'Interview':self.Interview,
            'Upload':self.Upload,
            'UserID':self.UserID,
            'dtUDate':self.dtUDate,
            'dtDate':self.dtDate,
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return ProductModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def product_find_by_str_name(DigiKeyPartNumber):
        return list(map(lambda x: x.json(), db.session.query(ProductModel).filter_by(DigiKeyPartNumber=DigiKeyPartNumber)))


ProductModel.create_db()
# CrawlerLogModel.select_crwlog(crwName='yyy')

# result = DBClass1Model.select_all()
# print(result)
