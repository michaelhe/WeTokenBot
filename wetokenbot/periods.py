# coding=utf-8

import datetime
from common.log import logger
from common.utils import get_token
from status import BotStatus
from config import MediaPlatforms

def refresh_access_token():
    """
    每一个小时执行一次，刷新access_token
    :return:
    """
    logger.info('RUN | refresh_access_token')
    for mp in MediaPlatforms:
        logger.info('GetToken | {}'.format(mp['name']))
        access_token = get_token(mp['appid'], mp['appsecret'])
        BotStatus.tokens.update({
            mp['name']: {
                'token': access_token,
                'refresh_time': datetime.datetime.now().strftime("%F %T")
            }
        })
