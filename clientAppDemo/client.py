#from PyQt5 import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
import connectServer

csw = connectServer.window()
csw.start()

app.exec()