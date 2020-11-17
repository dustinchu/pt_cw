from source.db import db
import json as js


class CrawlerRunSecModel(db.Model):
    __tablename__ = "crawlerRunSec"
    id = db.Column(db.Integer, primary_key=True)
    partNum = db.Column(db.String(100))
    crwSec = db.Column(db.String(100))
    postSec = db.Column(db.String(100))
    date = db.Column(db.String(100))

    def __init__(self, partNum, crwSec, postSec, date):
        self.partNum = partNum
        self.crwSec = crwSec
        self.postSec = postSec
        self.date = date

    def json(self):
        return {
            'partNum': self.partNum,
            'crwSec': self.crwSec,
            'postSec': self.postSec,
            'date': self.date,
        }

    def create_db():
        db.create_all()
        return CrawlerRunSecModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close


CrawlerRunSecModel.create_db()
