import socket
import os
import time
#import pyaudio
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

def checkPingAndSmthinElseSER(s: socket.socket, addr):
    data, address = s.recvfrom(4096)
    rcvTime = time.time()
    ping = (rcvTime - float(data.decode().split('|')[1])) * 1000
    print(ping)


def checkPingAndSmthinElseCLI(s: socket.socket, addr):
    message = b'A' * 10
    sendTime = time.time()
    payload = message.decode() + '|' + str(sendTime)
    s.sendto(payload.encode(), addr)

        

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

def sendAudio():    
    pass

def call():
    pass