from protocols.protocol import *

port = 5050
proxyip = str(socket.gethostbyname(socket.gethostname()))
addr = (proxyip, port)

psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
psocket.bind(addr)

spsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
spsocket.connect((proxyip, 1000))


def handleCLient(conn):
        
    while True:
        msg = recv(conn)
        send(spsocket, msg)
        print(msg)

#search for connections
psocket.listen()

conn, adr = psocket.accept()
print(adr)
handleCLient(conn)
