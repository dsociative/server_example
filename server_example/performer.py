# -*- coding: utf8 -*-
from class_collector import ClassCollector
from server_example.command.se_command import SECommand


class Performer(object):

    def init_mapper(self):
        return ClassCollector('server_example/command', SECommand).mapper()

    def __init__(self):
        self.mapper = self.init_mapper()

    def execute(self, params):
        command = self.get_command(params)
        if command:
            return command(params['cid'])(params)
        else:
            return {'error': 'not found command'}

    def get_command(self, params):
        return self.mapper.get(params.get('command'))