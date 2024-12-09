from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import pyqtSlot

class window(QWidget):
    
    def __init__(self, func1):
        super().__init__()
        self.pressedFunc = func1
        self.setGeometry(150,150,800,800)
        self.UiComponents()


    def UiComponents(self):
 
        # creating a push button
        button = QPushButton("connect", self)
 
        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)
 
        # adding action to a button
        button.clicked.connect(self.pressedFunc)

    def start(self):
        self.show()