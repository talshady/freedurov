import sqlite3
import json

#c++>
class dbtypes:
    id = 'INTEGER PRIMARY KEY AUTOINCREMENT'
    str = 'TEXT'
    int = 'INTEGER'

class conversation():
    cID: int
    uid1: int
    uid2: int
    def __init__(self, uID1, uID2, cursor: sqlite3.Cursor):
        if uID1 < uID2:
            temp = uID2
            uID2 = uID1
            uID1 = temp
        self.uid1 = uID1
        self.uid2 = uID2
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
        self.cursor.execute(f'SELECT msgs FROM conversations WHERE id = {self.cID}')
        msgs = self.cursor.fetchone()[0]
        if not msgs:
            msgs = ',' + str(last_msg_id)
        else:
            msgs += ',' + str(last_msg_id)
        self.cursor.execute("UPDATE conversations SET msgs = ? WHERE id = ?", ( msgs, self.cID ))
        
        #add message to unread messages by the other user
        recipientid = self.uid1 if uid == self.uid1 else self.uid2
        self.cursor.execute(f"SELECT id FROM unreadMessages WHERE uID = {recipientid}")
        rid = self.cursor.fetchone()
        if not rid:
            self.cursor.execute(f"INSERT INTO unreadMessages (msgs, uID) VALUES('NULL', {recipientid})")
            rid = self.cursor.lastrowid
        else:
            rid = rid[0]
        #db.coomit
        self.cursor.execute(f'SELECT msgs FROM unreadMessages WHERE id = {rid}')
        msgs = self.cursor.fetchone()[0]
        if msgs:
            msgs = ',' + str(last_msg_id)
        else:
            msgs += ',' + str(last_msg_id)
        self.cursor.execute('UPDATE unreadMessages set msgs = ? where id = ?',(msgs, rid))


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





class databaseManager2:
    db: sqlite3.connect
    cursor: sqlite3.Cursor
    def __init__(self):
        self.db = sqlite3.connect('messages.db')
        self.cursor = self.db.cursor()
        # Convs table create
        command = '''CREATE TABLE IF NOT EXISTS conversations
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    msgs TEXT, uID1 INTEGER, uID2 INTEGER)
        '''
        self.cursor.execute(command)

        # Msg table create
        command = '''CREATE TABLE IF NOT EXISTS messages
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    msg TEXT, uID INTEGER)
        '''
        self.cursor.execute(command)

        command = '''CREATE TABLE IF NOT EXISTS unreadMessages
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    msgs text, uID INTEGER)
        '''
        self.cursor.execute(command)
        
        self.db.commit()
    
    def openConversation(self, uID1, uID2):
        self.cconversation = conversation(uID1, uID2, self.cursor)
        self.db.commit()

    def writeMessage(self, msg, uid):
        self.cconversation.writeMessage(msg, uid)
        self.db.commit()

    def requestMessages(self, amn, i):
        self.cconversation.requestMessages(amn, i)


class databaseManager:
    db: sqlite3.connect
    cursor: sqlite3.Cursor
    dbname: str
    tname:str
    names = []
    def __init__(self, dbname ,tname, names, types):
        createCommand = "CREATE TABLE IF NOT EXISTS " + tname + '('
        for i in range(len(names)):
            createCommand += names[i] + ' ' + types[i] + ','
        print(createCommand)
        createCommand = createCommand[:-1] + ')'
        print(createCommand)
        self.db = sqlite3.connect(dbname + '.db')
        self.cursor = self.db.cursor()
        self.cursor.execute(createCommand)
        self.db.commit()

        self.names = names
        self.dbname = dbname
        self.tname = tname

    def getIdByName(self, column, val):
        command = 'SELECT '+ self.names[0] + ' FROM ' + self.tname + ' WHERE ' + column + ' = ' + val
        self.cursor.execute()

        
    def search(id):
        pass#dont need yet
    def insert(self, vals):
        command = 'INSERT INTO ' + self.tname + ' VALUES (NULL,'
        for v in vals:
            command += v + ','
        command = command[:-1] + ')'
        print(command)
        self.cursor.execute(command)
        self.db.commit()
    def handleList():
        #get the list
        pass

class users(databaseManager):
    def __init__(self):
        super().__init__('users', 'users', ['UID','username','password'],
                          [dbtypes.id, dbtypes.str, dbtypes.str])
        self.insert(['"t"','"test1"'])

#lc = latest conversations/channels/chats
class LCdbManager(databaseManager):
    def __init__(self):
        super().__init__('latestChats', 'lc', ['LID','UID','Conversations'], [dbtypes.id, dbtypes.int, dbtypes.str])
    
    
a = users()
    
    