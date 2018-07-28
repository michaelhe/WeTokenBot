# -*- coding=utf-8

# server监听的ip地址和端口号
IPAddr = '127.0.0.1'
Port = 8888

# access_token 周期刷新的时间，单位为ms
RefreshPeriodTime = 1000 * 3600

# 公众平台的配置信息, 多个公众平台以列表形式往后追加
MediaPlatforms = [
    {
        'name': u'mp_test_plat',
        'desc': u'公众号测试平台',
        'appid': 'xxxx', # 需要自己配置
        'appsecret': 'xxxx', # 需要自己配置
    },
]
