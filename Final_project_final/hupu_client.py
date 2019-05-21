import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5 import QtWidgets, QtCore
from client_interface import Ui_MainWindow
from chat_utils import mysend
import json
from client_stats import ClientStats

class HupuClient(QMainWindow, Ui_MainWindow):

    def __init__(self, s, name, parent=None):
        super(HupuClient, self).__init__(parent)
        self.setupUi(self)
        self.s = s
        self.name = name
        self.connect_button()
        self.stats = ClientStats()
        self.chance = 4

    def connect_button(self):
        self.post.clicked.connect(self.post_message)
        self.show_stats.clicked.connect(self.show_stats_interface)

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
        elif msg["update"] == "stats":
            self.stats.update_row(msg)
        self.repaint()
        
    def process(self,detail):
        lis = detail.split(' ')
        detail = ''
        state = False
        for i in lis:
            if i.lower() in ['arse','ass','asshole','bastard','bitch','bollocks','child-fucker','crap','cunt','damn','frigger','fuck','goddamn',\
                     'godsdamn','hell','holy shit','horseshit','motherfucker','nigga','nigger','prick','shit','slut','twat']:
                detail += '*'*len(i) + ' '
                state = True
            else:
                detail += i + ' '
        return detail,state

    def post_message(self):
        if self.input_new_line.text() != "":
            detail = self.input_new_line.text()
            if self.chance == 0:
                self.textBrowser.append('you are mute from hotline')
            else:
                if self.process(detail)[1]:
                    self.chance -= 1
                    detail = self.process(detail)[0]
                self.textBrowser.append("{}: {}".format(self.name, detail))
                self.input_new_line.setText("")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
                d = {"action": "broadcasting", "update": "chat", "detail": detail, "from": self.name}
                mysend(self.s, json.dumps(d))
                self.repaint()

    def show_stats_interface(self):
        self.stats.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = HupuClient(None, None)
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break
