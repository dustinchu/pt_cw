from source.db import db
import json as js


class CrawlerNameModel(db.Model):
    __tablename__ = "crawlerName"
    id = db.Column(db.Integer, primary_key=True)
    crwName = db.Column(db.String(100))
    category = db.Column(db.String(10))
    listName = db.Column(db.String(100))
    sPage = db.Column(db.String(100))
    ePage = db.Column(db.String(100))
    pageStatus = db.Column(db.String(1))

    def __init__(self, crwName, category, listName, sPage, ePage, pageStatus):
        self.crwName = crwName
        self.category = category
        self.listName = listName
        self.sPage = sPage
        self.ePage = ePage
        self.pageStatus = pageStatus

    def json(self):
        return {
            'crwName': self.crwName,
            'category': self.category,
            'listName': self.listName,
            'sPage': self.sPage,
            'ePage': self.ePage,
            'pageStatus': self.pageStatus,
        }

    def create_db():
        db.create_all()
        return CrawlerNameModel

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close

    def select_crwname(crwName, category):
        result = db.session.execute(
            "SELECT * FROM crawlerName  WHERE crwName='{crwName}' and category='{category}'  ORDER BY id"
            .format(crwName=crwName, category=category))
        if result.returns_rows:
            response = [dict(row.items()) for row in result]
        else:
            response = []
        rdata = js.dumps(response, ensure_ascii=False)
        return js.loads(rdata)


CrawlerNameModel.create_db()
# print(CrawlerNameModel.select_crwname('Connectors, Interconnects', '1'))

# for crawList in CrawlerNameModel.select_crwname('Connectors, Interconnects', '1'):
    # print(crawList)
    # print(crawList['listName'])
# print(CrawlerNameModel.select_ip())
