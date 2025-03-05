import socket
import protocol
import threading
#when connecting, to the caller, the server will send an id of
#recving part of the caller, and will open a recving line for himself

addr = (socket.gethostbyname(socket.gethostname()), 3333)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)

t = threading.Thread(target=protocol.checkPingAndSmthinElseSER, args=(server,addr))
t.start()   


addr = (socket.gethostbyname(socket.gethostname()), 4444)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

protocol.checkPingAndSmthinElseCLI(client, addr)

t.join()


#start recving and sending