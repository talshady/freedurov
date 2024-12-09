import dbManager


#messages are stored in conversations

#create a new conversation


messageidCounter = 0
#requests
def sendMessage(text, user):
    global messageidCounter
    messageidCounter += 1
    dbManager.writeMessage(dbManager.message(messageidCounter,
                                             text,user,5))





def requestMessages(user2):
    for i in range(6):
        print(dbManager.getMessage(i + 1))