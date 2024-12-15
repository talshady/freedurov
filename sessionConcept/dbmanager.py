import sqlite3

accountTable = ''' CREATE TABLE IF NOT EXISTS users
    (username TEXT, password TEXT)'''

db = sqlite3.connect('accounts.db')

cursor = db.cursor()

cursor.execute(accountTable)

db.commit()
def isUserNameExists(username):
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for u in users:
        if(u[0] == username):
            return True
    
    return False

def createNewUser(username, password):
    cursor.execute("INSERT INTO users VALUES ('" + username + "','" + password  + "')")
    db.commit()
    query = f"SELECT COUNT(*) FROM users"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]    

def getUidFromUsername(username):
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    i = 0
    for u in users:
        if(u[0] == username):
            return i
        i+=1

    return i
        
def getPassword(userid):
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return users[userid][1]