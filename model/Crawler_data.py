from source.db import db
import json as js
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func


class CrawlerFirstModel(db.Model):
    __tablename__ = "crawlerData"
    id = db.Column(db.Integer, primary_key=True)
    Categories = db.Column(db.String(100))
    Manufacturer = db.Column(db.String(100))
    Series = db.Column(db.String(100))
    Stock = db.Column(db.String(20))
    HomeName = db.Column(db.String(100))
    
    DigiKeyPartNumber = db.Column(db.String(100), index=True)
    PartNumber = db.Column(db.String(100), index=True)
    Description = db.Column(db.String(100))
    MetaDescription = db.Column(db.String(200))
    KeyWords = db.Column(db.String(200))
    body = db.Column(db.Text())
    price = db.Column(db.Text())
    datasheet = db.Column(db.Text())
    status = db.Column(db.String(10))
    updatetime = db.Column(
        DateTime, server_default=func.now(), onupdate=func.now(), index=True)

    def __init__(
            self, Categories, Manufacturer, Series, Stock, HomeName, DigiKeyPartNumber, PartNumber, Description, MetaDescription, KeyWords, body, price, datasheet, status):
        self.Categories = Categories
        self.Manufacturer = Manufacturer
        self.Series = Series
        self.Stock = Stock
        self.HomeName = HomeName
        self.DigiKeyPartNumber = DigiKeyPartNumber
        self.PartNumber = PartNumber
        self.Description = Description
        self.MetaDescription = MetaDescription
        self.KeyWords = KeyWords
        self.body = body
        self.price = price
        self.datasheet = datasheet
        self.status = status

    def json(self):
        return {
            'id': self.id,
            'Categories': self.Categories,
            'Manufacturer': self.Manufacturer,
            'Series': self.Series,
            'HomeName': self.HomeName,
            'DigiKeyPartNumber': self.DigiKeyPartNumber,
            'PartNumber': self.PartNumber,
            'Description': self.Description,
            'MetaDescription':self.MetaDescription,
            'KeyWords': self.KeyWords,
            'body': self.body,
            'price': self.price,
            'datasheet': self.datasheet,
            'status': self.status,

        }

    def create_db():
        db.create_all()
        return CrawlerFirstModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # db.session.close

    @classmethod
    def find_by_name(cls, PartNumber, DigiKeyPartNumber):
        return list(map(lambda x: x.json(), db.session.query(CrawlerFirstModel).filter_by(PartNumber=PartNumber, DigiKeyPartNumber=DigiKeyPartNumber)))
        # return cls.query.filter_by(PartNumber=name).first()

    @classmethod
    def find_by_home(cls, homeName):
        return list(map(lambda x: x.json(), db.session.query(CrawlerFirstModel).filter_by(HomeName=homeName)))

    @classmethod
    def update_to_db(cls, id, sql_json_arr):
        '''
         Stock = db.Column(db.String(20))
    HomeName = db.Column(db.String(100))
    PartNumber = db.Column(db.String(100))
    Description = db.Column(db.String(100))
    MetaDescription = db.Column(db.String(200))
    KeyWords = db.Column(db.String(200))
    body = db.Column(db.Text())
    price = db.Column(db.Text())
    datasheet = db.Column(db.Text())
    status = db.Column(db.String(10))
        '''
        try:
            db.session.query(CrawlerFirstModel).filter_by(id=id).update(
                {'Stock': sql_json_arr['Stock'], 'body': sql_json_arr['body'], 'price': sql_json_arr['price'], 'datasheet': sql_json_arr['datasheet'], 'status': sql_json_arr['status'], })
            db.session.commit()
            # db.session.close
            return {'status': 'ok'}
        except:
            return {'status': 'error'}
        # print("update  crawlerFirstDataNew set KeyWords='{KeyWords}', MetaDescription={MetaDescription}, Stock={qty}  WHERE PartNumber='{PartNumber}'".
        #       format(PartNumber=PartNumber, qty=qty, KeyWords=KeyWords, MetaDescription=MetaDescription))
        #     return {'status': sql}
        # except:
        #     return {'status': 'error'}
    @classmethod
    def select_post_data_crwname(cls):
        result = db.session.execute(
        "SELECT  id,Categories,Manufacturer,Series,Stock,HomeName,DigiKeyPartNumber,PartNumber,Description,MetaDescription,KeyWords,body,price,datasheet FROM crawlerdata WHERE STATUS ='NULL'  order by id LIMIT 50000")
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        # print(response)
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)

# user=CrawlerFirstModel(**a)
# user.save_to_db()
CrawlerFirstModel.create_db()
