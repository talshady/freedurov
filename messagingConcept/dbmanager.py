import sqlite3
import json





class conversation():
    cID: int
    def __init__(self, uID1, uID2, cursor: sqlite3.Cursor):
        if uID1 < uID2:
            temp = uID2
            uID2 = uID1
            uID1 = temp
        self.cursor = cursor
        self.cursor.execute('SELECT rowid FROM conversations WHERE uID1 = ' + str(uID1) + ' AND uID2 = ' + str(uID2))
        rid =self.cursor.fetchone()
        
        if not rid:
            cursor.execute(f'INSERT INTO conversations (msgs, uID1, uID2) VALUES(NULL, {uID1}, {uID2} )')
            rid = self.cursor.lastrowid
        else:
            rid = rid[0]
        self.cID = rid
        
        
    def writeMessage(self, msg, uid):
        msg = "'" + msg + "'"
        print(self.cID)
        self.cursor.execute(f'INSERT INTO messages (msg, uID) VALUES({msg}, {uid})')
        last_msg_id = self.cursor.lastrowid
        self.cursor.execute(f'SELECT msgs FROM conversations WHERE id = { self.cID }')
        msgs = self.cursor.fetchone()[0]
        msgs += ',' + str(last_msg_id)
        self.cursor.execute("UPDATE conversations SET msgs = ? WHERE id = ?", ( msgs, self.cID ))



    def requestMessages(self, amn, i):
        self.cursor.execute(f'SELECT msgs FROM conversations WHERE id = { self.cID }')
        msgs = self.cursor.fetchone()[0]
        msgs = msgs.split(',')
        msgs.pop(0)
        print(msgs)
        #do the len part later
        for i in range(len(msgs)):
            ind = int(msgs[i])
            self.cursor.execute(f'SELECT msg FROM messages WHERE id = { ind }')
            msg = self.cursor.fetchone()
            print(msg[0])



class databaseManager:
    db: sqlite3.connect
    cursor: sqlite3.Cursor
    def __init__(self):
        self.db = sqlite3.connect('messages.db')
        self.cursor = self.db.cursor()
        # Convs table create
        commnad = '''CREATE TABLE IF NOT EXISTS conversations
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    msgs TEXT, uID1 INTEGER, uID2 INTEGER)
        '''
        self.cursor.execute(commnad)

        # Msg table create
        commnad = '''CREATE TABLE IF NOT EXISTS messages
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    msg TEXT, uID INTEGER)
        '''
        self.cursor.execute(commnad)
        self.db.commit()
    
    def openConversation(self, uID1, uID2):
        self.cconversation = conversation(uID1, uID2, self.cursor)
        self.db.commit()

    def writeMessage(self, msg, uid):
        self.cconversation.writeMessage(msg, uid)
        self.db.commit()

    def requestMessages(self, amn, i):
        self.cconversation.requestMessages(amn, i)