from dbmanager import databaseManager

uID1 = 12343
uID2 = 1233
conversationsdb = databaseManager()
conversationsdb.openConversation(uID1, uID2)
conversationsdb.requestMessages(2,1)
#conversationsdb.requestMessages(6,0)
#conversationsdb.closeConversation()