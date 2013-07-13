# -*- coding: utf8 -*-


class SECommand(object):

    def __init__(self, cid):
        self.cid = cid

    def __call__(self, params):
        return self.execute(**params)

    def execute(self, params):
        raise Exception('template')