import dbmanager

class session:
    status = 'unverified'
    uid = 0

clientSession = session

def connect():
    clientSession = session

def Register(username, password):
    if clientSession.status != 'unlogged':
        print('unlogged')
        return
    if not dbmanager.isUserNameExists(username):
        uid = dbmanager.createNewUser(username, password)
        clientSession.status = 'logged'
        clientSession.uid = uid

def Login(username, password):
    if(dbmanager.isUserNameExists(username)):
        uid = dbmanager.getUidFromUsername(username)
        if(dbmanager.getPassword(uid) == password):
            clientSession.status = 'logged'
            clientSession.uid = uid
            return True
        
        return False

def printSession():
    print(clientSession.status)
    print(clientSession.uid)