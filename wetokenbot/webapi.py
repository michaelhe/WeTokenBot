# coding=utf-8

import tornado.web
from handlers.handler_main import HandlerMain
from handlers.handler_token import HandlerToken

def create_api():
    return tornado.web.Application([
        (r"/", HandlerMain),
        (r"/token", HandlerToken),
    ])