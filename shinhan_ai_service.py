import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from tkinter import *
from PyQt5 import uic, QtCore,QtGui,QtWidgets



form_class = uic.loadUiType("shinhan ai service.ui")[0]
form_class2 = uic.loadUiType("TermsOfUse.ui")[0]

class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # button event
        self.b1.clicked.connect(self.b1Function)
        self.b2.clicked.connect(self.b2Function)

        # create new screen when button clicked
    def b1Function(self):
        self.newWindow = NewWindow(self)
        self.newWindow.show()

    def b2Function(self):
        import wizard_shinhan_ai_service
        wizard_shinhan_ai_service.main()

class NewWindow(QMainWindow,form_class2):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)
        self.setupUi(self)
        self.setGeometry(40, 200, 720, 981)
        self.setWindowTitle("신한금융투자설명 AI 서비스")
        app.setWindowIcon(QIcon('logo.png'))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.setGeometry(850,300,700,470) #가로,세로 좌표 + 창 크기
    myWindow.setWindowTitle("신한금융투자설명 AI 서비스")
    app.setWindowIcon(QIcon('logo.png'))
    myWindow.show()
    app.exec_()
