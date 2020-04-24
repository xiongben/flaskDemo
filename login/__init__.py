
from flask import Blueprint,Flask,request
from flask_restful import Resource,Api, reqparse, fields, marshal_with
from bson.objectid import ObjectId
from model import LoginModel


# parser = reqparse.RequestParser()

class Login(Resource):
    def __init__(self):
        self.model = LoginModel()

    def get(self):
        # args = request.args
        # print args
        # params = {
        #     'user': args['name'],
        #     'password': args['password']
        # }
        try:
            # res = self.model.login(params)
            res = self.model.login()
            res = formaterRes(res)
            result = {'code':0,'data':res}
        except BaseException as error:
            result = {'code':1,'data':str(error)}   
        
        return result


class Register(Resource):
    def __init__(self):
        self.model = LoginModel()
    def get(self):
        args = request.args
        params = {
            'user': args['name'],
            'password': args['password']
        }
        print params
        try:
            res = self.model.register(params)
            result = {'code': 0, 'data': "success"}
        except BaseException as error:
            result = {'code': 1, 'data': str(error)}
        return result


def formaterRes(res):
    for item in res:
        if item.has_key('_id'):
            item['_id'] = str(item['_id'])
    return res