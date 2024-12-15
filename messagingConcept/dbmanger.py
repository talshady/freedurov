import sqlite3

#message table
messageTable = '''CREATE TABLE IF NOT EXISTS messages
    (mID INTEGER PRIMARY KEY, msg TEXT, uID INTEGER)'''

#conversation
#user1 id  = 321, user 2 id - 123
#when opening a conversation, open the class and it will be used for everything
class conversation:
    def __init__(self,user1Id, user2Id):
        self.db = sqlite3.connect('c3.db')
        self.cursor = db.cursor()
        self.i = 4
    
    def writeMessage(self, message, userId):
        self.i += 1
        msg = ''' ' ''' + message + ''' ' '''
        command = 'INSERT INTO messages(mID, msg, uID) VALUES(' + str(self.i) + ',' + msg + ' , ' + str(userId) + ')'
        self.cursor.execute(command)
        db.commit()

    def requestMessages(self, amount): #add i later
        command = 'SELECT * FROM messages'
        self.cursor.execute(command)
        messages = self.cursor.fetchmany(amount)
        for m in messages:
            print(m)


db = sqlite3.connect('test.db')


cursor = db.cursor()

cursor.execute(messageTable)

def writeMessage(txt):
    txt = ''' ' ''' + txt + ''' ' '''
    command = 'INSERT INTO messages VALUES(1,' + txt + ' ) '
    cursor.execute(command)
    db.commit()