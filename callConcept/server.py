import socket
import protocol

addr = (socket.gethostbyname(socket.gethostname()), 4444)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)

protocol.checkPingAndSmthinElseSER(server, addr)