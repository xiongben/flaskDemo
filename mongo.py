import pymongo

class Mongo(object):
    ___instance = None
    def __init__(self):
        pass
    @staticmethod
    def get_instance():
        if Mongo.___instance is None:
            url = 'mongodb://localhost:27017/'
            Mongo.___instance = pymongo.MongoClient(url).local
        return Mongo.___instance

def mongo():
    return Mongo.get_instance()  
