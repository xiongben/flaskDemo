from mongo import mongo
from bson.objectid import ObjectId


class UserModeldd:
    def __init__(self):
        self.mongo = mongo()

    def find(self,id):
        res = self.mongo.xiongben.find_one({'age':33})
        # print res[0]
        return res

    def add(self,**kw):
        raise RuntimeError('testError')
        data = kw
        id = {'_id' : ObjectId()}
        data2 = dict(id,**data)
        # _id = ObjectId()
        res = self.mongo.xiongben.insert(data2)
        return res

class TestModel:
    def __init__(self):
        pass

    def testxb(self):
        print 'testxb'


__all__ = ['UserModeldd', 'TestModel']