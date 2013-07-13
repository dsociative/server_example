# -*- coding: utf8 -*-
from server_example.performer import Performer
from tests.base_test import BaseTest


class PerformerTest(BaseTest):

    def setUp(self):
        super(PerformerTest, self).setUp()
        self.performer = Performer()

    def test_command(self):
        self.eq(
            self.performer.execute(
                {'command': 'join.list', 'list':[1, 2, 3], 'cid': 1}
            ),
            {'string': '123'}
        )

    def test_command_not_found(self):
        self.eq(
            self.performer.execute(
                {'command': 'not.found.command', 'list':[1, 2, 3], 'cid': 1}
            ),
            {'error': 'not found command'}
        )