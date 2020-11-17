
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func

class APILogModel(db.Model):
    __tablename__ = "api_log"
    PKey = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.Text())
    dtDate = db.Column(
    DateTime, server_default=func.now(), onupdate=func.now(), index=True)
    def __init__(self, contents):
        self.contents = contents
    def json(self):
        return {
            'contents': self.contents,
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return APILogModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def find_by_cookie():
        return list(map(lambda x: x.json(), db.session.query(APILogModel)))

    def delete_cookie(cookie):
        sql = "DELETE from   crawlercookie where cookie='{cookie}'".format(cookie=cookie)
        db.session.execute(sql)
        db.session.commit()
        return 'ok'

APILogModel.create_db()
