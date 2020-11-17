
from source.db import db
import json as js
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func

class CrawlerCookieModel(db.Model):
    __tablename__ = "crawlercookie"
    id = db.Column(db.Integer, primary_key=True)
    cookie = db.Column(db.Text())
    updatetime = db.Column(
    DateTime, server_default=func.now(), onupdate=func.now(), index=True)
    def __init__(self, cookie):
        self.cookie = cookie
    def json(self):
        return {
            'cookie': self.cookie,
        }

    def get_to_date():
        x = datetime.datetime.now()  # 現在時間
        return str(x.year) + str(x.month) + str(x.day)

    def create_db():
        db.create_all()
        return CrawlerCookieModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def find_by_cookie():
        return list(map(lambda x: x.json(), db.session.query(CrawlerCookieModel)))

    def delete_cookie(cookie):
        sql = "DELETE from   crawlercookie where cookie='{cookie}'".format(cookie=cookie)
        db.session.execute(sql)
        db.session.commit()
        return 'ok'

CrawlerCookieModel.create_db()
