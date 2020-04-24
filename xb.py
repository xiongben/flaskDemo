from flask import Flask,request,session,Response
from flask_socketio import SocketIO,emit,join_room,leave_room
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.debug = True



@app.route('/')
def index():
    # return render_template('index.html')
    res = Response("6666")
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080"
    res.headers['Access-Control-Allow-Credentials'] = "true"
    #res.set_cookie("xb", value='', max_age=None, expires=None, path='/', domain=None, secure=True, httponly=False, samesite='Lax')
    res.headers.add('Set-Cookie','cross-site-cookie=bar; SameSite=None; Secure')
    return res

@socketio.on('my event', namespace='/test')
def test_message(message):
    res =  message['mess']
    room = message['room']
    join_room(room)
    emit('myResponse', {'data': res}, room=room)

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('myResponse', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0',port=5000)

# import socket
# s = socket.socket()
# host = socket.gethostname()
# port = 12345
# ip_port = ('127.0.0.1',9999)
# s.bind(ip_port)
# s.listen(5)

# while True:
#     c, addr = s.accept()
#     print 'dizhi', addr
#     c.send('welcome,xiongben')
#     c.close()


