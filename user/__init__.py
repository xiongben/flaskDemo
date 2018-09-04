#-*- coding=utf-8 -*-
from flask import Blueprint,Flask,request
from flask_restful import Resource,Api, reqparse, fields, marshal_with
from user.model import UserModel
from user.admin import *
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId

parser = reqparse.RequestParser()
# parser.add_argument('name', type = dict,help = 'name must be string!')
# parser.add_argument('type', type = str,required = True,help = 'type must be string!')
parser.add_argument('type')
parser.add_argument('uid')
parser.add_argument('name')
parser.add_argument('tel')
parser.add_argument('email')
parser.add_argument('address')
parser.add_argument('skill')
parser.add_argument('age')


class User(Resource):
    def __init__(self):
        self.model = UserModel()
    def get(self):
        args = parser.parse_args()
        type = args['type']
        _id = ObjectId(args['uid'])
        res = self.model.find(_id)
        res['_id'] = str(res['_id'])
        return {'data':res,'type':args['type']}

    def post(self):
        args = parser.parse_args()
        try:
            res = self.model.add(name=args['name'],tel=args['tel'],email=args['email'],address=args['address'],age=args['age'],skill=args['skill'])
            result = {'code': 0, 'message': '', 'data': str(res)}
        except BaseException as error:
            result = {'code': 1, 'message': str(error)}
        return result
        # print res
        # res = str(res)
        # return {'data':res}





# def changeAge(id):
#     pass
