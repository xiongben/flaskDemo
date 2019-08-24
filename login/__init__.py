
from flask import Blueprint,Flask,request
from flask_restful import Resource,Api, reqparse, fields, marshal_with
from bson.objectid import ObjectId
from model import LoginModel


# parser = reqparse.RequestParser()

class Login(Resource):
    def __init__(self):
        self.model = LoginModel()

    def get(self):
        args = request.args
        print (args)
        params = {
            'user': args['name'],
            'password': args['password']
        }
        try:
            res = self.model.login(params)
            result = {'code':0,'data':str(res)}
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
        
        try:
            res = self.model.register(params)
            result = {'code': 0, 'data': "success"}
        except BaseException as error:
            result = {'code': 1, 'data': str(error)}
        return result