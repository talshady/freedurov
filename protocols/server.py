import protocol
import socket
import threading

#enums for request(no enums in python so minus ram😠😠😠)
requestCaptcha = 1
requestVerifyCaptcha = 2
requestLogin = 3
requestRegister = 4

class session:
    status = 'unverified'
    uID = None


port = 3333
ip = "0.0.0.0"
addr = (ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def handleCLient(client, addr):
    print("new connection!")
    #handshake?
    sessionKey = protocol.serHandShake(client)
    


    clientSession = session
    captcha = 'test'
    while True:
        r, a = protocol.recv(client, sessionKey)
        print(a)
        #check if r is int else say smthin
        if r == 1:
            if clientSession.status == 'unverified' or clientSession.status == 'requested captcha':
                print('sending captcha!')
                captcha = 'true test'

        if r == 2:
            if clientSession.status == 'requested captcha':
                if a == captcha:
                    clientSession.status = 'unlogged'
                    protocol.send(client, 51)           
        if r > 3 and clientSession.status == 'logged':
            pass
            #do follow the request or sum 


        #check for request and stuff

def start():
    server.listen()
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleCLient, args =(conn, addr))
        thread.start()

print('server is starting...')#mb animate

start()


#threading.activeCount() - 1 num of clients 