import socket
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend, openssl


HEADER = 64
FORMAT = 'utf-8'

requestCaptcha = 1
requestVerifyCaptcha = 2
requestLogin = 3
requestRegister = 4
IMGMSG = 10
IMGCHUNK = 1024


def enc(key, text):
    f = Fernet(key)
    return f.encrypt(text.encode(FORMAT))

def dec(key, text):
    f = Fernet(key)
    return f.decrypt(text).decode()


def serHandShake(s: socket.socket):
    pubM = s.recv(451)
    
    #generate symetic key
    key = Fernet.generate_key()
    
    print(key)

    #encrypt using the pubm
    pubK = serialization.load_pem_public_key(
        data=pubM,
        backend=default_backend()
        )
    
    encrypted = pubK.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(len(encrypted))
    #send encrypted symetric key
    s.send(encrypted)
 
    text = 'test'
    #handshake

    return key



def cliHandShake(s: socket.socket):
    privK = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048)
    pubK = privK.public_key()
    pubM = pubK.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)
    s.send(pubM)

    #recv encrypted symetric key
    encrypted = s.recv(256)

    #decrypt
    key = privK.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return key


def sendImg(s: socket.socket, path, format_callback):
    size = os.path.getsize(path)
    rawData = b''
    with open(path, 'rb') as f:
        rawData = format_callback( f.read( ) )

    r = str(size)
    r += " " * (HEADER - len(r))

    s.send( r.encode( ) )

    total = 0

    while total < size:
        rem = rawData[ total: ]
        size = min(IMGCHUNK, len(rem))
        chunk = rem[ :size ]

        s.send(chunk)
        total = total + size

def recvImg(s: socket.socket, format_callback):
    print("hell")
    size = str( s.recv( HEADER ) ).decode( )

    rec = b''
    while len(rec) < size:
        chunk = s.recv( min( size - len(rec), IMGCHUNK ) )
        rec += chunk
    
    file = "photo.png"

    rec = format_callback( rec )

    with open( file, "wb" ) as f:
        f.write(rec)

    

def send(s, r, msg, key, path=""):
    msglen = str(len(enc(key,msg))).encode(FORMAT) 
    msglen += b' ' * (HEADER - len(msglen)) 
    
    r = str(r).encode(FORMAT)
    r += b' ' * (HEADER - len(r))
    
    s.send(r)
    s.send(msglen)
    s.send(enc(key, msg))

    if r == IMGMSG:
        sendImg(s, path)


def recv(s, key):
    r = int(s.recv(HEADER).decode(FORMAT).strip())
    
    msglen = s.recv(HEADER).decode(FORMAT).strip()

    if msglen:
        msglen = int(msglen)  # Convert the length to integer
        msg = s.recv(msglen).decode(FORMAT)  # Receive the message

        if r == IMGMSG:
            recvImg(s)

        msg = dec(key, msg)
        return r, msg  # Return both 'r' and the message
    
    
    return "failed"

#free duruv pls pls