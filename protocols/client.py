import protocol
import socket

#enums for request(no enums in python so minus ram😠😠😠)
requestCaptcha = 1
requestVerifyCaptcha = 2
requestLogin = 3
requestRegister = 4

#enums for other stuff
image = 10


server = '192.168.138.1'
port = 7777
addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

protocol.send(client, requestCaptcha, 'test')
protocol.send(client, requestVerifyCaptcha, 'true test')

r,a = protocol.recv(client)
print(r)
print(a)

while True:
    pass