import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5 import QtWidgets, QtCore
from server_interface import Ui_MainWindow
from chat_utils import *
import json


class HupuSever(QMainWindow, Ui_MainWindow):

    def __init__(self, s, parent=None):

        super(HupuSever, self).__init__(parent)
        self.setupUi(self)

        self.s = s
        self.warning = QtWidgets.QDialog(self.centralwidget)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(118, 160, 341, 41))
        self.title.setStyleSheet("font: 15pt \"Arial\";")
        self.title.setObjectName("title")
        self.title.setText("Please Choose the Home and Guest Team to start.")
        self.vs_create = QtWidgets.QLabel(self.centralwidget)
        self.vs_create.setGeometry(QtCore.QRect(280, 220, 21, 16))
        self.vs_create.setObjectName("vs_create")
        self.vs_create.setText("vs")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(242, 266, 91, 32))
        self.create.setObjectName("create")
        self.create.setText("create")
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
        self.choose_China_home.setText("China")
        self.choose_America_home = QtWidgets.QPushButton(self.centralwidget)
        self.choose_America_home.setGeometry(QtCore.QRect(125, 320, 101, 32))
        self.choose_America_home.setObjectName("choose_America_home")
        self.choose_America_home.setText("America")
        self.choose_China_guest = QtWidgets.QPushButton(self.centralwidget)
        self.choose_China_guest.setGeometry(QtCore.QRect(345, 280, 101, 32))
        self.choose_China_guest.setObjectName("choose_China_guest")
        self.choose_China_guest.setText("China")
        self.choose_America_guest = QtWidgets.QPushButton(self.centralwidget)
        self.choose_America_guest.setGeometry(QtCore.QRect(345, 320, 101, 32))
        self.choose_America_guest.setObjectName("choose_America_guest")
        self.choose_America_guest.setText("America")
        
        self.ti = ''
        self.de = ''

        self.show_create()
        self.hide_main()
        self.connect_button()

    def connect_button(self):
        self.post.clicked.connect(self.add_text)
        self.create.clicked.connect(self.start)
        self.choose_America_guest.clicked.connect(lambda: self.choose_america(home=False))
        self.choose_America_home.clicked.connect(lambda: self.choose_america())
        self.choose_China_guest.clicked.connect(lambda: self.choose_china(home=False))
        self.choose_China_home.clicked.connect(lambda: self.choose_china())
        self.home_one.clicked.connect(lambda: self.add_point(1))
        self.home_two.clicked.connect(lambda: self.add_point(2))
        self.home_three.clicked.connect(lambda: self.add_point(3))
        self.guest_one.clicked.connect(lambda: self.add_point(1, home=False))
        self.guest_two.clicked.connect(lambda: self.add_point(2, home=False))
        self.guest_three.clicked.connect(lambda: self.add_point(3, home=False))

    def start(self):
        home_team = self.home_name.text()
        guest_team = self.guest_name.text()
        if home_team != "" and guest_team != "":
            self.home_icon.setStyleSheet("border-image: url(:/figure_lucy/{}.png);".format(home_team))
            self.guest_icon.setStyleSheet("border-image: url(:/figure_lucy/{}.png);".format(guest_team))
            self.show_main()
            self.hide_create()
            d = {"action": "broadcasting", "update": "start", "home": home_team, "guest": guest_team}
            mysend(self.s, json.dumps(d))
        else:
            QMessageBox.warning(self, "Warning", "Please select home/guest team before start.", QMessageBox.Ok)
        self.repaint()

    def hide_create(self):
        self.title.hide()
        self.home_name.hide()
        self.guest_name.hide()
        self.vs_create.hide()
        self.create.hide()
        self.choose_America_guest.hide()
        self.choose_America_home.hide()
        self.choose_China_guest.hide()
        self.choose_China_home.hide()
        self.Home_label_create.hide()
        self.Guest_label_create.hide()

    def show_create(self):
        self.title.show()
        self.home_name.show()
        self.home_name.show()
        self.vs_create.show()
        self.create.show()
        self.choose_America_guest.show()
        self.choose_America_home.show()
        self.choose_China_guest.show()
        self.choose_China_home.show()
        self.Home_label_create.show()
        self.Guest_label_create.show()

    def hide_main(self):
        self.textBrowser.hide()
        self.input_new_line.hide()
        self.home_icon.hide()
        self.guest_icon.hide()
        self.Home_label_main.hide()
        self.Guest_label_main.hide()
        self.vs_main.hide()
        self.post.hide()
        self.home_score.hide()
        self.guest_score.hide()
        self.colon.hide()
        self.home_one.hide()
        self.home_two.hide()
        self.home_three.hide()
        self.guest_one.hide()
        self.guest_two.hide()
        self.guest_three.hide()
        self.time.hide()
        self.input_time.hide()

    def show_main(self):
        self.textBrowser.show()
        self.input_new_line.show()
        self.home_icon.show()
        self.guest_icon.show()
        self.Home_label_main.show()
        self.Guest_label_main.show()
        self.vs_main.show()
        self.post.show()
        self.home_score.show()
        self.guest_score.show()
        self.colon.show()
        self.home_one.show()
        self.home_two.show()
        self.home_three.show()
        self.guest_one.show()
        self.guest_two.show()
        self.guest_three.show()
        self.time.show()
        self.input_time.show()

    def add_text(self):
        if self.input_time.text() != "" and self.input_new_line.text() != "":
            time = self.input_time.text()
            detail = self.input_new_line.text()
            self.ti = time
            self.de = detail
            self.textBrowser.append("{} : {}, {} : {}".format(time, detail, self.home_score.text(), self.guest_score.text()))
            self.time.setText(time)
            self.input_new_line.setText("")
            self.input_time.setText("")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            self.repaint()
            d = {"action": "broadcasting", "update": "post", "time": time, "detail": detail}
            mysend(self.s, json.dumps(d))

    def choose_china(self, home=True):
        if home:
            self.home_name.setText("China")
            # self.home_icon.setStyleSheet("border-image: url(:/figure_lucy/China.png);")
        else:
            self.guest_name.setText("China")
            # self.guest_icon.setStyleSheet("border-image: url(:/figure_lucy/China.png);")
        self.repaint()

    def choose_america(self, home=True):
        if home:
            self.home_name.setText("America")
            # self.home_icon.setStyleSheet("border-image: url(:/figure_lucy/America.png);")
        else:
            self.guest_name.setText("America")
            # self.guest_icon.setStyleSheet("border-image: url(:/figure_lucy/America.png);")
        self.repaint()

    def add_point(self, point, home=True):
        if home:
            self.home_score.setText(str(int(self.home_score.text()) + point))
        else:
            self.guest_score.setText(str(int(self.guest_score.text()) + point))
        d = {"action": "broadcasting", "update": "scored", "point": point, "home": home}
        mysend(self.s, json.dumps(d))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = HupuSever(None)
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break
