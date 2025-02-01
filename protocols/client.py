import protocol
import socket

#enums for request(no enums in python so minus ram😠😠😠)
requestCaptcha = 1
requestVerifyCaptcha = 2
requestLogin = 3
requestRegister = 4
IMGMSG = 10

#enums for other stuff
image = 10


server = '127.0.0.0'
port = 3333
addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

sessionKey = protocol.cliHandShake(client)
protocol.send(client, 0, 'test', sessionKey)
#protocol.send(client, IMGMSG, 'test', protocol.enc, path='CAPTCHA.png')

#r,a = protocol.recv(client, protocol.dec)

while True:
    pass