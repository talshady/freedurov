import socket

HEADER = 64
FORMAT = 'utf-8'


def send( s, msg):
    msglen = str(len(msg)).encode(FORMAT)
    msglen += b' ' * (HEADER - len(msglen))
    s.send(msglen)
    s.send(msg.encode(FORMAT))





def recv(s):
    msglen = s.recv(HEADER).decode(FORMAT)
    if msglen:
        msglen = int(msglen)
        msg = s.recv(msglen).decode(FORMAT)
        return msg
    return "failed"

    #free duruv