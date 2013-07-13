# -*- coding: utf8 -*-
from server_example.client import ServerExampleClient
from server_example.gateway import Gateway
from socket_server.base.talker import Talker
from tests.base_test import BaseTest


class GatewayTest(BaseTest):

    def setUp(self):
        super(GatewayTest, self).setUp()
        self.gateway = Gateway()

    def test_init_talker(self):
        self.isinstance(self.gateway.talker, Talker)
        self.eq(self.gateway.talker.client_cls, ServerExampleClient)