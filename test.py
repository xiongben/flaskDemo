#-*- coding=utf-8 -*-



from flask import Flask,request
from flask_restful import Resource,Api, reqparse, fields, marshal_with
from flask_cors import *

from flask_socketio import SocketIO, emit

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
        args = parser.parse_args()
        return {'hello':args['name']}
        

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

if __name__ == '__main__':
    app.run()
    