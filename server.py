from protocols.protocol import *

port = 1000
ip = str(socket.gethostbyname(socket.gethostname()))
addr = (ip,port)

ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssocket.bind(addr)

def handleClinet(conn):
    while(True):
        msg = recv(conn)
        print(msg)
        #print conn session

ssocket.listen()

conn, adr = ssocket.accept()
handleClinet(conn)