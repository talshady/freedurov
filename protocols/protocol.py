import socket

HEADER = 64
FORMAT = 'utf-8'

def send(s, r, msg):
    msglen = str(len(msg)).encode(FORMAT) 
    msglen += b' ' * (HEADER - len(msglen)) 
    
    r = str(r).encode(FORMAT)
    r += b' ' * (HEADER - len(r))

    s.send(r)
    s.send(msglen)
    s.send(msg.encode(FORMAT))



def recv(s):
    r = s.recv(HEADER).decode(FORMAT).strip()
    
    msglen = s.recv(HEADER).decode(FORMAT).strip()

    if msglen:
        msglen = int(msglen)  # Convert the length to integer
        msg = s.recv(msglen).decode(FORMAT)  # Receive the message
        return int(r), msg  # Return both 'r' and the message
    return "failed"
      
#free duruv pls