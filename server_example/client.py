# -*- coding: utf8 -*-
from server_example.performer import Performer
from socket_server.client.simple_client import SimpleClient


class ServerExampleClient(SimpleClient):

    performer = Performer()

    def listen(self, params):
        params['cid'] = self.id
        response = self.performer.execute(params)
        if response:
            self.add_resp(response)

    def disconnect(self, cid):
        print 'client', cid, 'disconnected'