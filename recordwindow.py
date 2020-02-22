# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

key = "2fbd0184b74d47af86b065ad503ab89f"
endpoint = "https://kpmg-text.cognitiveservices.azure.com/"


from PyQt5 import QtCore, QtGui, QtWidgets
from stt import SpeechToText
from Face import EmotionFace
from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
from capture import Capture

class Ui_recordWindow(object):

    All=''
    numclicked = 0
    Answer1 = ''
    Answer2 = ''
    Answer3 = ''
    
    

    def __init__(self):
        print("0")
        file=open('questions/question1.txt','r',encoding='utf-8-sig')
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
        MainWindow.setWindowTitle(_translate("MainWindow", "비대면상품ai서비스"))
        self.label.setText(_translate("MainWindow", "질문"))
        self.recordButton.setText(_translate("MainWindow", "녹음"))
        self.NextButton.setText(_translate("MainWindow", "다음"))

    def onrecordButtonClicked(self):
        print('record')
        if self.numclicked == 0:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('recording')
            msg.setText('recording')
            msg.show()
            stt = SpeechToText()
            img_name = "image{}".format(self.numclicked)
            img = Capture(img_name)
            self.Answer1 = stt.text
            msg.close()
        elif self.numclicked == 1:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('recording')
            msg.setText('recording')
            msg.show()
            stt = SpeechToText()
            img_name = "image{}".format(self.numclicked)
            img = Capture(img_name)
            self.Answer2 = stt.text
            msg.close()
        elif self.numclicked == 2:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('recording')
            msg.setText('recording')
            msg.show()
            stt = SpeechToText()
            img_name = "image{}".format(self.numclicked)
            img = Capture(img_name)
            self.Answer3 = stt.text
            msg.close()

    def onNextButtonClicked(self):
        if self.numclicked == 0:
            file=open('./questions/question2.txt','r', encoding='utf-8-sig')
            self.All=file.read()
            file.close()
            self.textBrowser.setText(self.All)
            self.numclicked = self.numclicked + 1

        elif self.numclicked == 1:
            file=open('./questions/question3.txt','r', encoding='utf-8-sig')
            self.All=file.read()
            file.close()
            self.textBrowser.setText(self.All)
            self.numclicked = self.numclicked + 1

        elif self.numclicked == 2:
            self.displayResult()

    def displayResult(self):
        text_analytics_client = TextAnalyticsClient(endpoint, TextAnalyticsApiKeyCredential(key))
        documents = [
            self.Answer1,
            self.Answer2,
            self.Answer3,
            
        ]

        response = text_analytics_client.analyze_sentiment(documents, language="ko")
        result = [doc for doc in response if not doc.is_error]

        for doc in result:
            print("Overall sentiment: {}".format(doc.sentiment))
            print("Scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
                doc.sentiment_scores.positive,
                doc.sentiment_scores.neutral,
                doc.sentiment_scores.negative,
            ))

        print("<----sentiment\n")



        response = text_analytics_client.extract_key_phrases(documents, language="ko")
        result = [doc for doc in response if not doc.is_error]

        for doc in result:
            print(doc.key_phrases)

    

        print("<----keyphrase\n")

        i = 0
        while i <= self.numclicked:
            img_name = "image{}.png".format(i)
            emotionresult = EmotionFace(img_name).emotions
            print('문제'+str(i)+emotionresult)
            i= i+1


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_recordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
