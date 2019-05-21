# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_interface.ui'
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
        self.Home_label_main = QtWidgets.QLabel(self.centralwidget)
        self.Home_label_main.setGeometry(QtCore.QRect(160, 145, 41, 16))
        self.Home_label_main.setObjectName("Home_label_main")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(166, 238, 256, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.vs_main = QtWidgets.QLabel(self.centralwidget)
        self.vs_main.setGeometry(QtCore.QRect(281, 79, 21, 31))
        self.vs_main.setStyleSheet("font: 20pt \"American Typewriter\";")
        self.vs_main.setObjectName("vs_main")
        self.Guest_label_main = QtWidgets.QLabel(self.centralwidget)
        self.Guest_label_main.setGeometry(QtCore.QRect(386, 145, 41, 16))
        self.Guest_label_main.setObjectName("Guest_label_main")
        self.home_icon = QtWidgets.QLabel(self.centralwidget)
        self.home_icon.setGeometry(QtCore.QRect(120, 60, 111, 71))
        self.home_icon.setStyleSheet("border-image: url(:/figure_lucy/America.png);")
        self.home_icon.setText("")
        self.home_icon.setObjectName("home_icon")
        self.guest_icon = QtWidgets.QLabel(self.centralwidget)
        self.guest_icon.setGeometry(QtCore.QRect(350, 60, 111, 71))
        self.guest_icon.setStyleSheet("border-image: url(:/figure_lucy/China.png);")
        self.guest_icon.setText("")
        self.guest_icon.setObjectName("guest_icon")
        self.home_score = QtWidgets.QLabel(self.centralwidget)
        self.home_score.setGeometry(QtCore.QRect(160, 188, 41, 21))
        self.home_score.setStyleSheet("font: 18pt \"Arial Black\";")
        self.home_score.setAlignment(QtCore.Qt.AlignCenter)
        self.home_score.setObjectName("home_score")
        self.guest_score = QtWidgets.QLabel(self.centralwidget)
        self.guest_score.setGeometry(QtCore.QRect(384, 188, 41, 21))
        self.guest_score.setStyleSheet("font: 18pt \"Arial Black\";")
        self.guest_score.setAlignment(QtCore.Qt.AlignCenter)
        self.guest_score.setObjectName("guest_score")
        self.colon = QtWidgets.QLabel(self.centralwidget)
        self.colon.setGeometry(QtCore.QRect(286, 188, 16, 21))
        self.colon.setStyleSheet("font: 18pt \"Arial Black\";")
        self.colon.setAlignment(QtCore.Qt.AlignCenter)
        self.colon.setObjectName("colon")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(257, 141, 71, 16))
        self.time.setStyleSheet("font: 18pt \"Arial Black\";")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.post = QtWidgets.QPushButton(self.centralwidget)
        self.post.setGeometry(QtCore.QRect(236, 482, 113, 32))
        self.post.setObjectName("post")
        self.input_new_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_new_line.setGeometry(QtCore.QRect(132, 458, 321, 21))
        self.input_new_line.setObjectName("input_new_line")
        self.show_stats = QtWidgets.QPushButton(self.centralwidget)
        self.show_stats.setGeometry(QtCore.QRect(236, 510, 113, 32))
        self.show_stats.setObjectName("show_stats")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home_label_main.setText(_translate("MainWindow", "Home"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the broadcasting room.</p></body></html>"))
        self.vs_main.setText(_translate("MainWindow", "vs"))
        self.Guest_label_main.setText(_translate("MainWindow", "Guest"))
        self.home_score.setText(_translate("MainWindow", "0"))
        self.guest_score.setText(_translate("MainWindow", "0"))
        self.colon.setText(_translate("MainWindow", ":"))
        self.time.setText(_translate("MainWindow", "12:00"))
        self.post.setText(_translate("MainWindow", "post"))
        self.show_stats.setText(_translate("MainWindow", "stats"))

import picture_lucy_rc
