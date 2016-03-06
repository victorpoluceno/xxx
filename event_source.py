import json

from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection


class EchoConnection(SockJSConnection):

    def __init__(self, *args, **kwargs):
        super(EchoConnection, self).__init__(*args, **kwargs)
        self.info_map = {}

    def on_open(self, info):
        self.info_map[self.session.session_id] = info

    def on_message(self, msg):
        info = self.info_map[self.session.session_id]
        event = json.loads(msg)
        event['extra']['ip'] = info.ip
        print('Got message, {0}'.format(event))


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    EchoRouter = SockJSRouter(EchoConnection, '/echo')

    app = web.Application(EchoRouter.urls)
    app.listen(9999)

    ioloop.IOLoop.instance().start()
