from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtCore,QtGui,QtWidgets
from tkinter import *


# CREATE WIZARD, LOGO, BANNER
app = QtWidgets.QApplication(sys.argv)
wizard = QtWidgets.QWizard()
wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)

try:  # PYSIDE
    wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
                     'Logo.png')
    wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
                     'Banner.png')
except TypeError:  # PYQT5
    wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
                     QtGui.QPixmap('Logo.png'))
    wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
                     QtGui.QPixmap('Banner.png'))

# CREATE PAGE 1, LINE EDIT, TITLES
page1 = QtWidgets.QWizardPage()
page1.setTitle('질문1.')
page1.setSubTitle('12개월 이내 자동 조기상환시, 수익률이 5.8%(약정 수익률)이하가 될 수 있나요?\n'
                  '(O/X로만 대답 바랍니다)')
lineEdit = QtWidgets.QLineEdit()
hLayout1 = QtWidgets.QHBoxLayout(page1)

#record button
page1.recordBtn = QtWidgets.QPushButton(wizard)
page1.recordBtn.setText("녹음하기")
page1.recordBtn.move(100,150)


# CREATE PAGE 2, LABEL, TITLES
page2 = QtWidgets.QWizardPage()
page2.setFinalPage(False)
page2.setTitle('질문2.')
page2.setSubTitle('만기 상환시, 원금 기초자산이 "몇 퍼센트 이하"일 경우 원금이 손실될까요?')
label = QtWidgets.QLabel()
hLayout2 = QtWidgets.QHBoxLayout(page2)
hLayout2.addWidget(label)


# CREATE PAGE 3, LABEL, TITLES
page3 = QtWidgets.QWizardPage()
page3.setFinalPage(False)
page3.setTitle('질문3.')
page3.setSubTitle('원금 손실시, "어떤 기초자산"을 기준으로 수익률을 책정할까요?')
label = QtWidgets.QLabel()
hLayout3 = QtWidgets.QHBoxLayout(page3)
hLayout3.addWidget(label)


# CREATE PAGE 4, LABEL, TITLES
page4 = QtWidgets.QWizardPage()
page4.setFinalPage(True)
page4.setTitle('비대면 AI 서비스가 종료되었습니다.')
page4.setSubTitle('')
label = QtWidgets.QLabel()
hLayout5 = QtWidgets.QHBoxLayout(page4)
hLayout5.addWidget(label)



# CONNECT SIGNALS AND PAGES
# lineEdit.textChanged.connect(lambda:label.setText(lineEdit.text()))
nxt = wizard.button(QtWidgets.QWizard.NextButton)
func = lambda: label.setText('')
nxt.clicked.connect(func)
wizard.addPage(page1)
wizard.addPage(page2)
wizard.addPage(page3)
wizard.addPage(page4)



if __name__ == "__main__" :
    wizard.setGeometry(850,300,700,500)
    wizard.setWindowTitle("신한금융투자설명 AI 서비스")
    app.setWindowIcon(QIcon('logo.png'))
    wizard.show()
    sys.exit(app.exec_())
