from datetime import datetime

class Scrap(object):
    def __init__(self, name, listUrl):
        self.name = name
        self.listUrl = listUrl
        self.lastModif = datetime.now()

    def to_dict(self):
        dest = {
            u'name': self.name,
            u'listUrl': self.listUrl,
            u'lastModif': self.lastModif
        }
        return dest