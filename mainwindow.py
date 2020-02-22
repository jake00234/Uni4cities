# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import webbrowser
from recordwindow import Ui_recordWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color:rgb(0, 39, 124)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sideimg.jpg"))
        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 8, 1)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.NextButton.clicked.connect(self.onNextButtonClicked)

        self.gridLayout_2.addWidget(self.NextButton, 7, 1, 1, 1)
        self.ShowPolicy = QtWidgets.QPushButton(self.centralwidget)
        self.ShowPolicy.setMouseTracking(False)
        self.ShowPolicy.setTabletTracking(False)
        self.ShowPolicy.setAcceptDrops(False)
        self.ShowPolicy.setAutoFillBackground(False)
        self.ShowPolicy.setStyleSheet("font: 14pt \".SF NS Text\"\n""")
        self.ShowPolicy.setCheckable(False)
        self.ShowPolicy.setAutoDefault(False)
        self.ShowPolicy.setFlat(False)
        self.ShowPolicy.setObjectName("ShowPolicy")
        self.ShowPolicy.clicked.connect(self.onShowPolicyButtonClicked)

        self.gridLayout_2.addWidget(self.ShowPolicy, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 14pt \".SF NS Text\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 15pt \".SF NS Text\";\n""")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "비대면상품ai서비스"))
        self.NextButton.setText(_translate("MainWindow", "Next >"))
        self.ShowPolicy.setText(_translate("MainWindow", "약관 보기"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>선택하신 상품은 비대면 상품확인 방법을 통해 지점방문(대면) 또는 ARS가 <br/>아닌 방식으로 인증하여 가입이 가능한 서비스를 제공합니다.</p><p>반드시 본인만 서비스를 통한 인증이 가능(내국민 개인에 한함)하며,<br/>마이크와 카메라가 있는 환경에서 이용해주시기 바랍니다.</p><p>아래의 &lt;약관 보기&gt; 버튼을 눌러 약관을 숙지 후 다음화면을 실행하세요.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">신한금융투자설명 AI 서비스 이용안내</span></p></body></html>"))

    def onShowPolicyButtonClicked(self):
        print('clicked')
        webbrowser.open_new('policy.pdf')

    def onNextButtonClicked(self):
        print('clicked')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recordWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
