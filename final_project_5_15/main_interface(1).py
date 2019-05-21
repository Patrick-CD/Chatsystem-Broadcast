# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 254, 256, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.input_new_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_new_line.setGeometry(QtCore.QRect(120, 163, 341, 21))
        self.input_new_line.setObjectName("input_new_line")
        self.post = QtWidgets.QPushButton(self.centralwidget)
        self.post.setGeometry(QtCore.QRect(230, 203, 113, 32))
        self.post.setObjectName("post")
        self.home_icon = QtWidgets.QLabel(self.centralwidget)
        self.home_icon.setGeometry(QtCore.QRect(136, 44, 81, 71))
        self.home_icon.setStyleSheet("background-color: rgb(252, 0, 11);")
        self.home_icon.setText("")
        self.home_icon.setObjectName("home_icon")
        self.vs_main = QtWidgets.QLabel(self.centralwidget)
        self.vs_main.setGeometry(QtCore.QRect(284, 64, 21, 31))
        self.vs_main.setStyleSheet("font: 20pt \"American Typewriter\";")
        self.vs_main.setObjectName("vs_2")
        self.guest_icon = QtWidgets.QLabel(self.centralwidget)
        self.guest_icon.setGeometry(QtCore.QRect(366, 44, 81, 71))
        self.guest_icon.setStyleSheet("background-color: rgb(252, 0, 11);")
        self.guest_icon.setText("")
        self.guest_icon.setObjectName("guest_icon")
        self.Guest_label_main = QtWidgets.QLabel(self.centralwidget)
        self.Guest_label_main.setGeometry(QtCore.QRect(386, 130, 41, 16))
        self.Guest_label_main.setObjectName("Guest_label")
        self.Home_label_main = QtWidgets.QLabel(self.centralwidget)
        self.Home_label_main.setGeometry(QtCore.QRect(160, 130, 41, 16))
        self.Home_label_main.setObjectName("Home_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the broadcasting room.</p></body></html>"))
        self.post.setText(_translate("MainWindow", "post"))
        self.vs_main.setText(_translate("MainWindow", "vs"))
        self.Guest_label_main.setText(_translate("MainWindow", "Guest"))
        self.Home_label_main.setText(_translate("MainWindow", "Home"))

