# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_stats.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class ClientStats(QDialog):

    def __init__(self):
        super(ClientStats, self).__init__()
        self.setObjectName("Dialog")
        self.resize(515, 182)
        self.row = 0
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 601, 192))
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

        self.map_dic = {}
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def update_row(self, msg):
        if msg["number"] not in self.map_dic.keys():
            self.row += 1
            self.tableWidget.setRowCount(self.row)

            item = QtWidgets.QTableWidgetItem()
            item.setText(msg["number"])
            self.tableWidget.setVerticalHeaderItem(self.row - 1, item)

            points = QtWidgets.QTableWidgetItem()
            points.setText(msg["points"])
            self.tableWidget.setItem(self.row - 1, 0, points)

            three_pt = QtWidgets.QTableWidgetItem()
            three_pt.setText(msg["three_pt"])
            self.tableWidget.setItem(self.row - 1, 1, three_pt)

            two_pt = QtWidgets.QTableWidgetItem()
            two_pt.setText(msg["two_pt"])
            self.tableWidget.setItem(self.row - 1, 2, two_pt)

            free_throw = QtWidgets.QTableWidgetItem()
            free_throw.setText(msg["free_throw"])
            self.tableWidget.setItem(self.row - 1, 3, free_throw)

            total = QtWidgets.QTableWidgetItem()
            total.setText(msg["total"])
            self.tableWidget.setItem(self.row - 1, 4, total)
        else:
            row = self.map_dic[msg["number"]]
            self.tableWidget.item(row, 0).setText(msg["points"])
            self.tableWidget.item(row, 1).setText(msg["three_pt"])
            self.tableWidget.item(row, 2).setText(msg["two_pt"])
            self.tableWidget.item(row, 3).setText(msg["free_throw"])
            self.tableWidget.item(row, 4).setText(msg["total"])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
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

