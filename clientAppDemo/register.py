from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow,QLabel,QVBoxLayout,QLineEdit


class window(QMainWindow):
    def __init__(self, pressedFunc, pressedFunc2):
        super().__init__()
        self.pressedFunc = pressedFunc
        self.pressedFunc2 = pressedFunc2
        self.ui()

    def ui(self):
        self.resize(500,500)
        self.label = QtWidgets.QLabel('register', self)
        self.label.setGeometry(120, 20, 47, 13)
        self.label2 = QtWidgets.QLabel('username', self)
        self.label2.setGeometry(100, 70, 47, 13)
        self.label3 = QtWidgets.QLabel('password', self)
        self.label3.setGeometry(100, 120, 47, 13)
        self.untextbox = QLineEdit(self)
        self.pwtextbox = QLineEdit(self)
        self.untextbox.setGeometry(100, 90, 113, 20)
        self.pwtextbox.setGeometry(100, 140, 113, 20)
        self.registerButton = QPushButton('register', self)
        self.registerButton.setGeometry(100, 190, 75, 23)
        self.registerButton.clicked.connect(self.pressedRegister)
        self.fwloginButton = QPushButton('old user?', self)
        self.fwloginButton.setGeometry(270, 250, 72, 23)
        self.fwloginButton.clicked.connect(self.pressedFunc2)

    def pressedRegister(self):
        username = self.untextbox.text()
        password = self.pwtextbox.text()
        self.pressedFunc(username, password)

    def start(self):
        self.show()