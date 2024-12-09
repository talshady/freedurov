from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow,QLabel,QVBoxLayout,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets,QtCore

from PyQt5.QtCore import pyqtSlot

class window(QMainWindow):
    
    def __init__(self, pressedFunc):
        super().__init__()
        self.pressedFunc = pressedFunc
        self.setWindowTitle("captcha")
        #self.pressedFunc = func1
        self.setGeometry(10,10,1000,1000)
        self.UiComponents()
    def UiComponents(self):
        label = QLabel(self)
        pixmap = QPixmap('captcha.png')

        # Check if the image was loaded successfully
        if pixmap.isNull():
            print("Error: Could not load image.")
        else:
            label.setPixmap(pixmap)
            label.resize(pixmap.width(), pixmap.height())
        self.textbox = QLineEdit(self)
        self.textbox.move(500, 500)
        self.textbox.resize(280,40)

        #buttn
        button = QPushButton("send captcha", self)
        button.setGeometry(350, 470, 100, 30)
        button.clicked.connect(self.pressedCaptcha)

    def pressedCaptcha(self):
        self.pressedFunc(self.textbox.text())

    def start(self):
        self.show()