from dbmanager import databaseManager

uID1 = 12343
uID2 = 1233
conversationsdb = databaseManager()


clientID = 1234
def openConversation(uid):
    conversationsdb.openConversation(clientID, uid)

def writeMessage(msg):
    conversationsdb.writeMessage(msg, clientID)

def requestMessages():
    pass

conversationsdb.openConversation(666, 999)
conversationsdb.writeMessage('plspls work', 999)

#close conversation
#fix the conversation opening closing its shit