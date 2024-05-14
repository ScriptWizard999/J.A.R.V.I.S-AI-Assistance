from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUI(object):
    def setupUi(self, jarvisUI):
        jarvisUI.setObjectName("jarvisUI")
        jarvisUI.resize(1496, 760)
        self.centralwidget = QtWidgets.QWidget(jarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1531, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/downloads/38119.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(970, 10, 631, 421))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/downloads/MImN.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 40, 581, 341))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:/downloads/jarvis_jj.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 540, 441, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:/downloads/initial.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 570, 181, 61))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 18pt \"Old English Text MT\";\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 640, 181, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 18pt \"Old English Text MT\";\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 471, 281))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:/downloads/Code_Template.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 310, 461, 251))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:/downloads/live.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 430, 261, 161))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:/downloads/Jarvis_Gui (1).gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(880, 520, 341, 221))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("D:/downloads/Earth_Template.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1160, 500, 341, 261))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("D:/downloads/B.G_Template_1.gif"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        jarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisUI)

    def retranslateUi(self, jarvisUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisUI.setWindowTitle(_translate("jarvisUI", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUI", "START"))
        self.pushButton_2.setText(_translate("jarvisUI", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisUI()
    ui.setupUi(jarvisUI)
    jarvisUI.show()
    sys.exit(app.exec_())
