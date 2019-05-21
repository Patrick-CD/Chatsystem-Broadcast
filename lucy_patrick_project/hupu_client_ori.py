import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5 import QtWidgets, QtCore
from client_interface import Ui_MainWindow


class HupuClient(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(HupuClient, self).__init__(parent)
        self.setupUi(self)

    def update_board(self, msg):
        if msg["update"] == "start":
            home_team = msg["home"]
            guest_team = msg["guest"]
            self.home_icon.setStyleSheet("border-image: url(:/figure_lucy/{}.png);".format(home_team))
            self.guest_icon.setStyleSheet("border-image: url(:/figure_lucy/{}.png);".format(guest_team))
        elif msg["update"] == "post":
            time = msg["time"]
            detail = msg["detail"]
            self.textBrowser.append("{} : {}, {} : {}".format(time, detail, self.home_score.text(), self.guest_score.text()))
            self.time.setText(time)
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        elif msg["update"] == "scored":
            point = msg["point"]
            home = msg["home"]
            if home:
                self.home_score.setText(str(int(self.home_score.text()) + point))
            else:
                self.guest_score.setText(str(int(self.guest_score.text()) + point))
        elif msg["update"] == "end":
            self.hide()
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = HupuClient(None)
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break
