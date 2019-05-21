import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5 import QtWidgets, QtCore
from main_interface import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(120, 200, 341, 41))
        self.title.setStyleSheet("font: 15pt \"Arial\";")
        self.title.setObjectName("title")
        self.title.setText("Please Enter the Home and Guest Team to start.")
        self.input_home = QtWidgets.QLineEdit(self.centralwidget)
        self.input_home.setGeometry(QtCore.QRect(120, 260, 101, 21))
        self.input_home.setObjectName("input_home")
        self.input_guest = QtWidgets.QLineEdit(self.centralwidget)
        self.input_guest.setGeometry(QtCore.QRect(340, 260, 101, 21))
        self.input_guest.setObjectName("input_guest")
        self.vs_create = QtWidgets.QLabel(self.centralwidget)
        self.vs_create.setGeometry(QtCore.QRect(274, 260, 21, 16))
        self.vs_create.setObjectName("vs")
        self.vs_create.setText("vs")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(220, 320, 113, 32))
        self.create.setObjectName("create")
        self.create.setText("create")
        self.Home_label_create = QtWidgets.QLabel(self.centralwidget)
        self.Home_label_create.setGeometry(QtCore.QRect(151, 290, 41, 16))
        self.Home_label_create.setObjectName("Home_label")
        self.Guest_label_create = QtWidgets.QLabel(self.centralwidget)
        self.Guest_label_create.setGeometry(QtCore.QRect(370, 290, 41, 16))
        self.Guest_label_create.setObjectName("Guest_label")

        self.show_create()
        self.hide_main()
        self.connect_button()

    def connect_button(self):
        self.post.clicked.connect(self.add_text)
        self.create.clicked.connect(self.start)

    def start(self):
        self.show_main()
        self.hide_create()
        home_team = self.input_home.text()
        guest_team = self.input_guest.text()
        self.home_icon.setText(home_team)
        self.guest_icon.setText(guest_team)
        self.repaint()

    def hide_create(self):
        self.title.hide()
        self.input_home.hide()
        self.input_guest.hide()
        self.vs_create.hide()
        self.create.hide()
        self.Home_label_create.hide()
        self.Guest_label_create.hide()

    def show_create(self):
        self.title.show()
        self.input_home.show()
        self.input_guest.show()
        self.vs_create.show()
        self.create.show()
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

    def show_main(self):
        self.textBrowser.show()
        self.input_new_line.show()
        self.home_icon.show()
        self.guest_icon.show()
        self.Home_label_main.show()
        self.Guest_label_main.show()
        self.vs_main.show()
        self.post.show()

    def add_text(self):
        self.textBrowser.append(self.input_new_line.text())
        self.input_new_line.setText("")
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow(None)
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break
