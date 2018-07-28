# -*- coding=utf-8

import requests
from common.log import logger

def get_token(appid, appsec):
    """
    通过appid和appsec来获取access_token
    :param appid: 公众号的appid
    :param appsec: 公众号的appsecret
    :return: string
    """
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    payload = {
        'grant_type' : 'client_credential',
        'appid': appid,
        'secret': appsec,
    }
    resp = requests.get(url, params=payload, timeout=1, verify=True)
    if 'access_token' not in resp.json():
        logger.error('GetToken ERROR: {}'.format(resp.json()))
        return ''
    return resp.json()['access_token']