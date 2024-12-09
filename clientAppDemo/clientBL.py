from PyQt5.QtWidgets import QApplication, QWidget #vctava ctrana agrmonya
import sys #vctavai na smertni boj

app = QApplication(sys.argv) #s fashistskoi siloi temnoio

#S prokliatoio ordoi.

def _on_pressedRegister(username, password):
    print(username)
    print(password)

def _on_fwPressedLogin():
    lw.start()
    rw.close()

import register 
rw = register.window(_on_pressedRegister, _on_fwPressedLogin)

def _on_loginPressed(username, password):
    print(username)
    print(password)

def _on_fwRegisterPressed():
    lw.close()
    rw.start()

import login 
lw = login.window(_on_loginPressed,_on_fwRegisterPressed)
    
def _on_pressedCaptcha(insertedCaptcha):
    print(insertedCaptcha)
    #check if captcha is right
    cw.close()
    lw.start()

import captcha 
cw = captcha.window(_on_pressedCaptcha)

#added functions
def _on_pressedConnect(): 
    print("connecting....")
    #try to connect to server
    csw.close()
    cw.start()
 
import connectServer 
csw = connectServer.window(_on_pressedConnect)

csw.start()

#connecting to server







app.exec()