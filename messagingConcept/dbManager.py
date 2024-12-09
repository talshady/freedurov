currentMid = 0

class message:
    def __init__(self,mid,msg, uid,gid):
        self.mid = mid
        self.msg = msg
        self.uid = uid
        self.gid = gid
        self.len = len(msg)#len of how it will be stored 6 for number
    
def writeMessage(message):
    f = open('database.txt', 'a')
    f.write( f"{message.len:06d}" + f"{message.mid:06d}" 
            + f"{message.uid:06d}" + f"{message.gid:06d}" + message.msg)
    f.close()

def getMessage(mid): #for now just the message content
    ind = 0
    f = open('database.txt','r')
    for i in range(mid - 1):
        f.seek(ind)
        len = int(f.read(6))
        ind +=  len + 24
            
    f.seek(ind)
    msglen = int(f.read(6))
    f.seek(ind + 24) 
    msg = f.read(msglen)
    f.close()
    return msg


