from source.db import db
import json as js


class CrawlerOnlineModel(db.Model):
    __tablename__ = "crawlerOnline"
    id = db.Column(db.Integer, primary_key=True)
    crwTitle = db.Column(db.String(100))
    crwName = db.Column(db.String(100))
    DigiKeyPartNumber = db.Column(db.String(100), index=True)
    partNum = db.Column(db.String(100), index=True)
    page = db.Column(db.Integer)
    onlineIndex = db.Column(db.Integer)

    def __init__(self, crwTitle, crwName, DigiKeyPartNumber, partNum, page, onlineIndex):
        self.crwTitle = crwTitle
        self.crwName = crwName
        self.DigiKeyPartNumber = DigiKeyPartNumber
        self.partNum = partNum
        self.page = page
        self.onlineIndex = onlineIndex

    def json(self):
        return {
            'crwTitle': self.crwTitle,
            'crwName': self.crwName,
            'DigiKeyPartNumber': self.DigiKeyPartNumber,
            'partNum': self.partNum,
            'page': self.page,
            'onlineIndex': self.onlineIndex,
        }

    def create_db():
        db.create_all()
        return CrawlerOnlineModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # db.session.close

    def select_crwOnline(crwTitle, index):
        result = db.session.execute(
            "SELECT * FROM crawlerOnline  WHERE crwTitle='{crwTitle}' and onlineIndex = '{index}'"
            .format(crwTitle=crwTitle, index=index))
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)
    
    def update_crwOnline(crwTitle, crwName, partNum, page, index, DigiKeyPartNumber):
        sql = "UPDATE  crawlerOnline SET page = '{page}'  , crwName='{crwName}', partNum='{partNum}', DigiKeyPartNumber='{DigiKeyPartNumber}' WHERE crwTitle='{crwTitle}'  and onlineIndex='{index}'".format(
            crwTitle=crwTitle,
            crwName=crwName,
            page=page,
            partNum=partNum,
            DigiKeyPartNumber=DigiKeyPartNumber,
            index=index)
        db.session.execute(sql)
        db.session.commit()
        # db.session.close

    def delete_crwOnline(crwTitle,  index):
        sql = "DELETE from   crawlerOnline where crwTitle='{crwTitle}' and onlineIndex='{index}' ".format(
            crwTitle=crwTitle, index=index)
        db.session.execute(sql)
        db.session.commit()
        # db.session.close


CrawlerOnlineModel.create_db()
