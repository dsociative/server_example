# -*- coding: utf8 -*-
from server_example.command.join.join_list import JoinList
from tests.base_test import BaseTest


class JoinListTest(BaseTest):

    def setUp(self):
        super(JoinListTest, self).setUp()
        self.command = JoinList(1)

    def params(self):
        return {'list': ['h', 1, '2m']}

    def test_command(self):
        self.eq(self.command(self.params()), {'string': 'h12m'})
