# -*- coding: utf8 -*-
from server_example.command.se_command import SECommand


class JoinList(SECommand):

    name = 'join.list'
    params = 'list',

    def execute(self, list, **kw):
        return {'string': ''.join(map(str, list))}