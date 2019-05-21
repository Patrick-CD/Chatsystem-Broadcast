# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
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
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(118, 160, 341, 41))
        self.title.setStyleSheet("font: 15pt \"Arial\";")
        self.title.setObjectName("title")
        self.vs_create = QtWidgets.QLabel(self.centralwidget)
        self.vs_create.setGeometry(QtCore.QRect(280, 220, 21, 16))
        self.vs_create.setObjectName("vs_create")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(242, 266, 91, 32))
        self.create.setObjectName("create")
        self.Home_label_create = QtWidgets.QLabel(self.centralwidget)
        self.Home_label_create.setGeometry(QtCore.QRect(157, 250, 41, 16))
        self.Home_label_create.setObjectName("Home_label_create")
        self.Guest_label_create = QtWidgets.QLabel(self.centralwidget)
        self.Guest_label_create.setGeometry(QtCore.QRect(376, 250, 41, 16))
        self.Guest_label_create.setObjectName("Guest_label_create")
        self.home_name = QtWidgets.QLabel(self.centralwidget)
        self.home_name.setGeometry(QtCore.QRect(135, 220, 81, 20))
        self.home_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_name.setText("")
        self.home_name.setObjectName("home_name")
        self.guest_name = QtWidgets.QLabel(self.centralwidget)
        self.guest_name.setGeometry(QtCore.QRect(356, 220, 81, 20))
        self.guest_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.guest_name.setText("")
        self.guest_name.setObjectName("guest_name")
        self.choose_China_home = QtWidgets.QPushButton(self.centralwidget)
        self.choose_China_home.setGeometry(QtCore.QRect(125, 280, 101, 32))
        self.choose_China_home.setObjectName("choose_China_home")
        self.choose_America_home = QtWidgets.QPushButton(self.centralwidget)
        self.choose_America_home.setGeometry(QtCore.QRect(125, 320, 101, 32))
        self.choose_America_home.setObjectName("choose_America_home")
        self.choose_China_guest = QtWidgets.QPushButton(self.centralwidget)
        self.choose_China_guest.setGeometry(QtCore.QRect(345, 280, 101, 32))
        self.choose_China_guest.setObjectName("choose_China_guest")
        self.choose_America_guest = QtWidgets.QPushButton(self.centralwidget)
        self.choose_America_guest.setGeometry(QtCore.QRect(345, 320, 101, 32))
        self.choose_America_guest.setObjectName("choose_America_guest")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Please Choose the Home and Guest Team to start."))
        self.vs_create.setText(_translate("MainWindow", "vs"))
        self.create.setText(_translate("MainWindow", "Create"))
        self.Home_label_create.setText(_translate("MainWindow", "Home"))
        self.Guest_label_create.setText(_translate("MainWindow", "Guest"))
        self.choose_China_home.setText(_translate("MainWindow", "China"))
        self.choose_America_home.setText(_translate("MainWindow", "America"))
        self.choose_China_guest.setText(_translate("MainWindow", "China"))
        self.choose_America_guest.setText(_translate("MainWindow", "America"))

