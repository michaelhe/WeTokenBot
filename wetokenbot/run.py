# coding=utf-8

import tornado.ioloop
from common.log import logger
from webapi import create_api
from config import RefreshPeriod
from periods import refresh_access_token

if __name__ == "__main__":
    api = create_api()
    address = '127.0.0.1'
    port = 8888
    api.listen(address=address, port=port)
    logger.info('app start at http://{}:{}'.format(address, port))
    refresh_access_token() # 先执行一次，后面才会周期调用
    tornado.ioloop.PeriodicCallback(refresh_access_token, 1000 * 3600).start()
    logger.info('PeriodicCallback start success')
    tornado.ioloop.IOLoop.instance().start()
