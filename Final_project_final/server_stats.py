# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_stats.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from chat_utils import *
import json


class ServerStats(QDialog):

    def __init__(self, s):
        super(ServerStats, self).__init__()
        self.s = s
        self.row = 0
        self.map_dic = {}
        self.setObjectName("Dialog")
        self.resize(766, 182)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 511, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(580, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.three_pt = QtWidgets.QPushButton(self)
        self.three_pt.setGeometry(QtCore.QRect(580, 50, 113, 32))
        self.three_pt.setObjectName("three_pt")
        self.two_pt = QtWidgets.QPushButton(self)
        self.two_pt.setGeometry(QtCore.QRect(580, 90, 113, 32))
        self.two_pt.setObjectName("two_pt")
        self.free_throw = QtWidgets.QPushButton(self)
        self.free_throw.setGeometry(QtCore.QRect(580, 130, 113, 32))
        self.free_throw.setObjectName("free_throw")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connect_button()

    def connect_button(self):
        self.three_pt.clicked.connect(lambda: self.update_stats(3))
        self.two_pt.clicked.connect(lambda: self.update_stats(2))
        self.free_throw.clicked.connect(lambda: self.update_stats(1))

    def update_a_and_m(self, r, c, m):
        made, attempt = tuple(self.tableWidget.item(r, c).text().split("/"))
        attempt = str(int(attempt) + 1)
        if m:
            made = str(int(made) + 1)
        self.tableWidget.item(r, c).setText(made + "/" + attempt)
        self.repaint()

    def update_stats(self, point):
        text = self.lineEdit.text().split()

        if len(text) > 0:
            number = text[0]
            if len(text) > 1:
                made = True
            else:
                made = False
        else:
            number = ""
        if number != "":
            self.lineEdit.setText("")
            if number in self.map_dic.keys():
                row = self.map_dic[number]
            else:
                row = self.row
                self.map_dic[number] = self.row
                self.tableWidget.setRowCount(self.row + 1)

                item = QtWidgets.QTableWidgetItem()
                item.setText(number)
                self.tableWidget.setVerticalHeaderItem(self.row, item)

                points = QtWidgets.QTableWidgetItem()
                points.setText("0")
                self.tableWidget.setItem(self.row, 0, points)

                three_pt = QtWidgets.QTableWidgetItem()
                three_pt.setText("0/0")
                self.tableWidget.setItem(self.row, 2, three_pt)

                two_pt = QtWidgets.QTableWidgetItem()
                two_pt.setText("0/0")
                self.tableWidget.setItem(self.row, 1, two_pt)

                free_throw = QtWidgets.QTableWidgetItem()
                free_throw.setText("0/0")
                self.tableWidget.setItem(self.row, 3, free_throw)

                total = QtWidgets.QTableWidgetItem()
                total.setText("0/0")
                self.tableWidget.setItem(self.row, 4, total)
                self.row += 1

            if made:
                self.tableWidget.item(row, 0).setText(str(int(self.tableWidget.item(row, 0).text()) + point))
            if point == 3:
                self.update_a_and_m(row, 2, made)
            elif point == 2:
                self.update_a_and_m(row, 1, made)
            elif point == 1:
                self.update_a_and_m(row, 3, made)
            self.update_a_and_m(row, 4, made)

            self.repaint()
            d = {"action": "broadcasting", "update": "stats","number":number,
                 "points": self.tableWidget.item(row, 0).text(),
                 "three_pt": self.tableWidget.item(row, 2).text(),
                 "two_pt": self.tableWidget.item(row, 1).text(),
                 "free_throw": self.tableWidget.item(row, 3).text(),
                 "total": self.tableWidget.item(row, 4).text()}
            mysend(self.s, json.dumps(d))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "points"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2pt(a/m)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "3pt(a/m)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "free throw(a/m)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "total(a/m)"))
        self.three_pt.setText(_translate("Dialog", "three"))
        self.two_pt.setText(_translate("Dialog", "two"))
        self.free_throw.setText(_translate("Dialog", "free_throw"))

