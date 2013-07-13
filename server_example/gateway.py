# -*- coding: utf8 -*-
from server_example.client import ServerExampleClient
from socket_server.base.talker import Talker


class Gateway(object):

    def __init__(self):
        self.talker = Talker(port=9342, client_cls=ServerExampleClient)

    def start(self):
        self.talker.run()