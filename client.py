# import socket
# s = socket.socket()
# host = socket.gethostname()
# print host
# port = 12345
# ip_port = ('127.0.0.1',9999)
# s.connect(ip_port)
# print s.recv(1024)
# s.close()

# a = [2,3,4,5]
# b = [3,8,9,33]
# print list(set(b).difference(set(a)));
# print list(set(a).difference(set(b)));

# x,y = 10, 20
# print(x, y)
# y, x = x, y
# print(x, y)
# n = 10
# print(1<n<=9)

# y=10
# x=9 if(y == 10) else 8
# print(x)

# def small(a,b,c):
#     return a if a<b and a<c else(b if b<a and b<c else c)

# print(small(3,4,5))

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "hello,xb"