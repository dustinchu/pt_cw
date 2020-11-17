from source.db import db
import json as js


class CrawlerVPNModel(db.Model):
    __tablename__ = "ipaddress"
    id = db.Column(db.Integer, primary_key=True)
    connectData = db.Column(db.String(500))
    county = db.Column(db.String(100))
    online_id = db.Column(db.String(50))

    def __init__(self, connectData, county, online_id):
        self.connectData = connectData
        self.county = county
        self.online_id = online_id

    def json(self):
        return {
            'connectData': self.connectData,
            'county': self.county,
            'online_id':self.online_id
        }

    def create_db():
        db.create_all()
        return CrawlerVPNModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def select_conndctData(connectData):
        result = db.session.execute(
            "SELECT * FROM ipaddress  WHERE connectData='{connectData}'".
            format(connectData=connectData))
        if result.returns_rows == False:
            response = []
        else:
            response = [dict(row.items()) for row in result]
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)

    def select_ip():
        result = db.session.execute("SELECT * FROM ipaddress where online_id is  NULL")
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)

    def delete_ip(connectData):
        sql = "DELETE from ipaddress WHERE connectData='{connectData}'".format(
            connectData=connectData)
        db.session.execute(sql)
        db.session.commit()
        db.session.close

    def update_ip(online_id,connectData):
        if online_id is None:
            sql = "UPDATE  ipaddress SET online_id = NULL WHERE connectData='{connectData}'".format(connectData=connectData)
        else:
            sql = "UPDATE  ipaddress SET online_id = '{online_id}' WHERE connectData='{connectData}'".format(online_id=online_id,connectData=connectData)
        db.session.execute(sql)
        db.session.commit()
        db.session.close


# CrawlerVPNModel.create_db()
# print(CrawlerVPNModel.select_ip())
