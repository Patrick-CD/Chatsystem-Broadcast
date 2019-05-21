"""
Created on Sun Apr  5 00:00:32 2015

@author: zhengzhang
"""
from chat_utils import *
import json
import sys
from hupu_client import HupuClient
from hupu_server import HupuSever
from PyQt5.QtWidgets import QApplication


class ClientSM:
    def __init__(self, s):
        self.state = S_OFFLINE
        self.peer = ''
        self.me = ''
        self.out_msg = ''
        self.s = s
        self.app = QApplication(sys.argv)
        self.hupu_server = None
        self.hupu_client = None
        self.stats_h = {'number':['ponits','assists','rebounds','attempts','made','3-attempt','3-made','ft','ft-made','fouls']}
        self.stats_g = {'number':['ponits','assists','rebounds','attempts','made','3-attempt','3-made','ft','ft-made','fouls']}
        
    def stat(self,msg):
        try:
            lis = msg.split(',')
            if lis[0] == 'h':
                try:
                    a = self.stats_h[lis[1]]
                except:
                    self.stats_h[lis[1]] = [0,0,0,0,0,0,0,0,0,0]
                for i in lis[2:]:
                    if i == 'p2':
                        self.stats_h[lis[1]][0] += 2
                    elif i == 'p1':
                        self.stats_h[lis[1]][0] += 1
                    elif i == 'p3':
                        self.stats_h[lis[1]][0] += 3
                    elif i == 'a':
                        self.stats_h[lis[1]][1] += 1
                    elif i == 'r':
                        self.stats_h[lis[1]][2] += 1
                    elif i == 'at':
                        self.stats_h[lis[1]][3] += 1
                    elif i == '3at':
                        self.stats_h[lis[1]][3] += 1
                        self.stats_h[lis[1]][5] += 1
                    elif i == 'fa':
                        self.stats_h[lis[1]][7] += 1
                    elif i == 'm':
                        self.stats_h[lis[1]][4] += 1
                    elif i == '3m':
                        self.stats_h[lis[1]][6] += 1
                    elif i == 'fm':
                        self.stats_h[lis[1]][8] += 1
                    elif i == 'f':
                        self.stats_h[lis[1]][9] += 1
            elif lis[0] == 'g':
                try:
                    a = self.stats_g[lis[1]]
                except:
                    self.stats_g[lis[1]] = [0,0,0,0,0,0,0,0,0,0]
                for i in lis[2:]:
                    if i == 'p2':
                        self.stats_g[lis[1]][0] += 2
                    elif i == 'p1':
                        self.stats_h[lis[1]][0] += 1
                    elif i == 'p3':
                        self.stats_g[lis[1]][0] += 3
                    elif i == 'a':
                        self.stats_g[lis[1]][1] += 1
                    elif i == 'r':
                        self.stats_g[lis[1]][2] += 1
                    elif i == 'at':
                        self.stats_g[lis[1]][3] += 1
                    elif i == '3at':
                        self.stats_g[lis[1]][3] += 1
                        self.stats_g[lis[1]][5] += 1
                    elif i == 'fa':
                        self.stats_g[lis[1]][7] += 1
                    elif i == 'm':
                        self.stats_g[lis[1]][4] += 1
                    elif i == '3m':
                        self.stats_g[lis[1]][6] += 1
                    elif i == 'fm':
                        self.stats_g[lis[1]][8] += 1
                    elif i == 'f':
                        self.stats_g[lis[1]][9] += 1
            else:
                return False
            return True
        except:
            return False
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_myname(self, name):
        self.me = name

    def get_myname(self):
        return self.me

    def connect_to(self, peer):
        msg = json.dumps({"action":"connect", "target":peer})
        mysend(self.s, msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.peer = peer
            self.out_msg += 'You are connected with '+ self.peer + '\n'
            return (True)
        elif response["status"] == "busy":
            self.out_msg += 'User is busy. Please try again later\n'
        elif response["status"] == "self":
            self.out_msg += 'Cannot talk to yourself (sick)\n'
        else:
            self.out_msg += 'User is not online, try again later\n'
        return(False)

    def disconnect(self):
        msg = json.dumps({"action":"disconnect"})
        mysend(self.s, msg)
        self.out_msg += 'You are disconnected from ' + self.peer + '\n'
        self.peer = ''
        
    
            

    def proc(self, my_msg, peer_msg):
        self.out_msg = ''
#==============================================================================
# Once logged in, do a few things: get peer listing, connect, search
# And, of course, if you are so bored, just go
# This is event handling instate "S_LOGGEDIN"
#==============================================================================
        if self.state == S_LOGGEDIN:
            # todo: can't deal with multiple lines yet
            if len(my_msg) > 0:

                if my_msg == 'q':
                    self.out_msg += 'See you next time!\n'
                    self.state = S_OFFLINE

                elif my_msg == 'time':
                    mysend(self.s, json.dumps({"action":"time"}))
                    time_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += "Time is: " + time_in


                elif my_msg == 'who':
                    mysend(self.s, json.dumps({"action":"list"}))
                    logged_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += 'Here are all the users in the system:\n'
                    self.out_msg += logged_in

                elif my_msg[0] == 'c':
                    peer = my_msg[1:]
                    peer = peer.strip()
                    self.peer = peer
                    if self.connect_to(peer) == True:
                        self.state = S_CHATTING
                        self.out_msg += 'Connect to ' + peer + '. Chat away!\n\n'
                        self.out_msg += '-----------------------------------\n'
                    else:
                        self.out_msg += 'Connection unsuccessful\n'

                elif my_msg[0] == '?':
                    term = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"search", "target":term}))
                    search_rslt = json.loads(myrecv(self.s))["results"][0:].strip()
                    if (len(search_rslt)) > 0:
                        self.out_msg += search_rslt + '\n\n'
                    else:
                        self.out_msg += '\'' + term + '\'' + ' not found\n\n'

                elif my_msg[0] == 'p':
                    poem_idx = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"poem", "target":poem_idx}))
                    poem = json.loads(myrecv(self.s))["results"][0:].strip()
                    if (len(poem) > 0):
                        self.out_msg += poem + '\n\n'
                    else:
                        self.out_msg += 'Sonnet ' + poem_idx + ' not found\n\n'

                else:
                    self.out_msg += menu

            if len(peer_msg) > 0:
                peer_msg = json.loads(peer_msg)

                if peer_msg["action"] == "connect":
                    name = peer_msg["from"]
                    self.peer = name
                    self.out_msg += "Hello, {0}".format(name)
                    self.state = S_CHATTING

#==============================================================================
# Start chatting, 'bye' for quit
# This is event handling instate "S_CHATTING"
#==============================================================================
        elif self.state == S_CHATTING:
            if len(my_msg) > 0:     # my stuff going out

                if my_msg == "broadcasting":
                    self.app.startingUp()
                    self.hupu_server = HupuSever(self.s)
                    self.state = S_POSTER
                    self.hupu_server.show()
                
                elif my_msg == "Official":
                    self.state = S_STATS
                    print('welcome stat official')
                    

                else:
                    mysend(self.s, json.dumps({"action": "exchange", "from": "[" + self.me + "]", "message": my_msg}))
                    if my_msg == 'bye':
                        self.disconnect()
                        self.state = S_LOGGEDIN
                        self.peer = ''

            if len(peer_msg) > 0:    # peer's stuff, coming in
                peer_msg = json.loads(peer_msg)
                if peer_msg["action"] == "exchange":
                    print("coming message from {0}: {1}".format(peer_msg["from"], peer_msg["message"]))
                elif peer_msg["action"] == "disconnect":
                    self.state = S_LOGGEDIN
                elif peer_msg["action"] == "connect":
                    name = peer_msg["from"]
                    self.out_msg += "Hello, {0}".format(name)
                elif peer_msg['action'] == 'stats':
                    stats = peer_msg['message']
                    
                elif peer_msg["action"] == "broadcasting" and self.state != S_STATS and peer_msg["update"] == "start":
                    self.state = S_LISTNER
                    self.hupu_client = HupuClient(None)
                    self.app.startingUp()
                    self.hupu_client.show()
                    self.hupu_client.update_board(peer_msg)
                    self.app.processEvents()

            # Display the menu again
            if self.state == S_LOGGEDIN:
                self.out_msg += menu
        elif self.state == S_POSTER:
            self.app.processEvents()
            my_msg = self.hupu_server.de
            if self.hupu_server.isHidden():
                d = {"action": "broadcasting", "update": "end"}
                mysend(self.s, json.dumps(d))
                self.state = S_CHATTING
                print("Back to normal chatting state.")
            if my_msg == 'show':
                self.hupu_server.textBrowser.append(str(self.stats_g) + str(self.stats_h))
                self.hupu_server.repaint()
            if len(peer_msg) > 0:
                peer_msg = json.loads(peer_msg)
                if peer_msg['action'] == 'stats':
                    self.stat(peer_msg['message'])
                
        elif self.state == S_STATS:
            if len(my_msg) > 0:
                print("""input format: h/g(home/guest),num(number),p1/p2/p3(1point/2points/3points),a(assist),r(rebound),\
                      at/3at/fa(attempt/three att/freethrow),m/3m/fm(made/three made/freethrow),f(foul)\
                      """)
                if self.stat(my_msg):
                    mysend(self.s, json.dumps({"action": "stats", "from": "[" + self.me + "]", "message": my_msg}))
                    print('success')
                else:
                    print('wrong format')
                if my_msg == 'bye':
                    self.disconnect()
                    self.state = S_LOGGEDIN
                    self.peer = ''
                elif my_msg == 'show':
                    print(self.stats_h)
                    print(self.stats_g)
            

        elif self.state == S_LISTNER:
            if len(peer_msg) > 0:
                peer_msg = json.loads(peer_msg)
                if peer_msg['action'] == 'broadcasting':
                    if peer_msg['update'] == 'post':
                        if peer_msg['detail'] == 'show':
                            peer_msg['detail'] = str(self.stats_h) + str(self.stats_g)
                        self.hupu_client.update_board(peer_msg)
                    else:
                        self.hupu_client.update_board(peer_msg)
                elif peer_msg['action'] == 'Listening':
                    self.hupu_client.update_board(peer_msg)
                elif peer_msg['action'] == 'stats':
                    self.stat(peer_msg['message'])
                
            self.app.processEvents()
            if self.hupu_client.isHidden():
                self.app.processEvents()
                self.state = S_CHATTING
                print("Back to normal chatting state.")
#==============================================================================
# invalid state
#==============================================================================
        else:
            self.out_msg += 'How did you wind up here??\n'
            print_state(self.state)

        return self.out_msg
