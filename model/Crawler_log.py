
from source.db import db
import json as js
import datetime


class CrawlerLogModel(db.Model):
    __tablename__ = "crawlerLog"
    id = db.Column(db.Integer, primary_key=True)
    crwTitle = db.Column(db.String(100))
    crwName = db.Column(db.String(100))
    count = db.Column(db.Integer)
    crwDate = db.Column(db.String(10))
    crwIndex = db.Column(db.Integer)
    def __init__(self, crwTitle, crwName, count, crwDate, crwIndex):
        self.crwTitle = crwTitle
        self.crwName = crwName
        self.count = count
        self.crwDate = crwDate
        self.crwIndex = crwIndex
    def json(self):
        return {
            'crwTitle': self.crwTitle,
            'crwName': self.crwName,
            'count': self.count,
            'crwDate': self.crwDate,
            'crwIndex': self.crwIndex,
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return CrawlerLogModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def select_crwlog(crwName, crwIndex):
        x = datetime.datetime.now()  # 現在時間
        date = str(x.year) + str(x.month) + str(x.day)
        result = db.session.execute(
            "SELECT * FROM crawlerLog  WHERE crwName='{crwName}' and crwDate='{crwDate}' and crwIndex ='{crwIndex}' order by id".
            format(crwName=crwName, crwDate=date, crwIndex=crwIndex))
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)

    def update_crwlog(crwName, count, crwIndex):
        x = datetime.datetime.now()
        date = str(x.year) + str(x.month) + str(x.day)
        sql = "UPDATE  crawlerLog SET count = '{count}' WHERE crwName='{crwName}' and crwDate='{crwDate}' and crwIndex='{crwIndex}' ".format(
            crwName=crwName, count=count, crwDate=date, crwIndex=crwIndex)
        db.session.execute(sql)
        db.session.commit()
        db.session.close

    def select_sum_count():
        x = datetime.datetime.now()  # 現在時間
        date = str(x.year) + str(x.month) + str(x.day)
        result = db.session.execute(
            "SELECT crwTitle,SUM(COUNT) as count FROM crawlerlog  WHERE crwDate='{crwDate}'  GROUP BY crwTitle".
            format(crwDate=date))
        print("result==={}".format(result))
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        
        # rdata = js.dumps(response, ensure_ascii=False)
        # print(rdata)
        # return js.loads(rdata)
        return response


CrawlerLogModel.create_db()
# CrawlerLogModel.select_crwlog(crwName='yyy')
