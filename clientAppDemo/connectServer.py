from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import pyqtSlot

class window(QWidget):
    
    def __init__(self):
        QWidget.__init__(10,10,1000,1000)

    def UiComponents(self):
 
        # creating a push button
        button = QPushButton("CLICK", self)
 
        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)
 
        # adding action to a button
        button.clicked.connect(self.clickme)
 
    # action method
    def clickme(self):
 
        # printing pressed
        print("pressed")
    
    def start(self):
        self.show()