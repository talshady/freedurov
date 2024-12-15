import dbmanger

c = dbmanger.conversation(1,2)

def RequestConvversation():
    messages = c.requestMessages(5)

def sendMessage(msg):
    c.writeMessage(msg,5)

#dbmanger.writeMessage('test', 5)