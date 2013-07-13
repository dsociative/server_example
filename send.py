#!env/bin/python
# -*- coding: utf8 -*-
from socket_server.util.sender import Sender

if __name__ == '__main__':
    sender = Sender('', 9342)
    sender.connect()
    sender.send({'command': 'join.list', 'list': [1, 2, 3, 'qwe']})
    print sender.recv()