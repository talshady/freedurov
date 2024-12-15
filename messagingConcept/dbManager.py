currentMid = 0


class message:
    def __init__(self,mid,msg, uid,gid):
        self.mid = mid
        self.msg = msg
        self.uid = uid
        self.gid = gid
        self.len = len(msg)#len of how it will be stored 6 for number

    def writeMessage(self,1):
        f = open('database.txt', 'a')
        f.write( f"{self.len:06d}"    + f"{self.mid:06d}" + f"{self.uid:06d}" + f"{self.gid:06d}" + self.msg       )
        f.close()

    def readMessage(self, mid):
        ind = 0
        f = open('database.txt','r')
        for i in range(mid - 1):
            ind +=  int(f.read(6)) + 24
        
        f.seek(ind)
        msglen = int(f.read(6))
        f.seek(ind + 24)
        print(f.read(msglen))
        f.close
        

        
firstmessage = message(3,'have you seen who won the election?', 123,321)
message.writeMessage()
#firstmessage.readMessage(1)
#firstmessage.readMessage(2)
#firstmessage.readMessage(3)
#firstmessage.readMessage(4)
