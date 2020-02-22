# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from stt import SpeechToText


class Ui_recordWindow(object):

    All=''
    numclicked = 0
    Answer1 = ''
    Answer2 = ''
    Answer3 = ''

    def __init__(self):
        print("0")
        file=open('./questions/question1.txt','r')
        self.All=file.read()
        file.close()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 70, 721, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(self.All)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 61))
        self.label.setObjectName("label")
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setGeometry(QtCore.QRect(40, 280, 111, 41))
        self.recordButton.setObjectName("recordButton")
        self.recordButton.clicked.connect(self.onrecordButtonClicked)

        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setGeometry(QtCore.QRect(650, 280, 111, 41))
        self.NextButton.setObjectName("NextButton")
        self.NextButton.clicked.connect(self.onNextButtonClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.recordButton.setText(_translate("MainWindow", "녹음"))
        self.NextButton.setText(_translate("MainWindow", "다음"))

    def onrecordButtonClicked(self):
        print('record')
        if self.numclicked == 0:
            stt = SpeechToText()
            self.Answer1 = stt.text
        elif self.numclicked == 1:
            stt = SpeechToText()
            self.Answer2 = stt.text
        elif self.numclicked == 2:
            stt = SpeechToText()
            self.Answer3 = stt.text

    def onNextButtonClicked(self):
        if self.numclicked == 0:
            file=open('./questions/question2.txt','r')
            self.All=file.read()
            file.close()
            self.textBrowser.setText(self.All)
            self.numclicked = self.numclicked + 1

        elif self.numclicked == 1:
            file=open('./questions/question3.txt','r')
            self.All=file.read()
            file.close()
            self.textBrowser.setText(self.All)
            self.numclicked = self.numclicked + 1

        #elif #need adjusment




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_recordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
