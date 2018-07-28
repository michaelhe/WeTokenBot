# coding=utf-8

import tornado.web
from status import BotStatus
import json

class HandlerToken(tornado.web.RequestHandler):
    """
    处理token的类
    """
    
    def get(self):
        name = self.get_argument('name')
        self.write(json.dumps(BotStatus.tokens.get(name, {})))