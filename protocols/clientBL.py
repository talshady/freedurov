from protocols.protocol import *

server = socket.gethostbyname(socket.gethostname())
port = 5050
addr = (server, port)

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csocket.connect(addr)

send(csocket,"hi")
while True:
    print(1)