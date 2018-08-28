import socket
s = socket.socket()
host = socket.gethostname()
print host
port = 12345
ip_port = ('127.0.0.1',9999)
s.connect(ip_port)
print s.recv(1024)
s.close()