from mongo import mongo
from bson.objectid import ObjectId

class LoginModel:
    def __init__(self):
        self.mongo = mongo()

    def login(self, params):

        # res = self.mongo.user_login.find_one({'name':params['user'],'password':params['password']})
        res = self.mongo.user_login.find_one({'name':params['user'],'password': params['password']},{'name':1,'_id':0})
        print res
        return res

    def register(self, params):
        res = self.mongo.user_login.insert(params)
        return res