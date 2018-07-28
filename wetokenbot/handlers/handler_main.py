# coding=utf-8

import tornado.web
from status import BotStatus

class HandlerMain(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world, run times: {}".format(BotStatus.run_times))