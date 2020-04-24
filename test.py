#-*- coding=utf-8 -*-



from flask import Flask,request
from flask_restful import Resource,Api, reqparse, fields, marshal_with
from flask_cors import *

from flask_socketio import SocketIO, emit
import logging
from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import SQLAlchemy

#logging set
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

rHandler = RotatingFileHandler("log.txt",maxBytes=1*1024,backupCount=3)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(rHandler)
logger.addHandler(console)

# handle = logging.FileHandler('flask.txt')
# handle.setLevel(logging.INFO)

# handle.setFormatter(formatter)
# logger.addHandler(handle)
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("something maybe fail")
# logger.info("Finish")


# from user import User
from user import *
from login import *


print TestModel

resource_fields = {
    'task': fields.String,
    'status': fields.String,
    'uri':  fields.Url('todo_ep')
}


parser = reqparse.RequestParser()
parser.add_argument('name', type = str,help = 'name must be string!')


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.debug = True


app.config['SECRET_KEY'] ='hard to guess'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:xB$12345678@127.0.0.1:3306/flasktest'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#实例化
db = SQLAlchemy(app)


api = Api(app)

todos = {}



# @app.route('/')
# def hello_world():
#     return 'hello world'
class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    
    def get(self,**kwargs):
        return TodoDao(todo_id = 'my_todo', task = 'Remember the milk')


class HelloWorld(Resource):
    def get(self):
        # logger.info('info log');
        # logger.warning("something maybe fail,test,xiongben")
        return {'hello': 'you'}
        # return {'hello':args['name']}
        

class TodoSimple(Resource):
    def get(self,todo_id):
        return {todo_id:todos[todo_id]}

    def put (self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

api.add_resource(HelloWorld,'/')
api.add_resource(Todo,'/resourse/aa',endpoint = 'todo_ep')
api.add_resource(TodoSimple, '/todo/<string:todo_id>')

api.add_resource(User,'/User','/User/<string:id>')
api.add_resource(TestModel,'/User/test')

# login area
api.add_resource(Login,'/login')
api.add_resource(Register,'/register')

if __name__ == '__main__':
    app.run()
    