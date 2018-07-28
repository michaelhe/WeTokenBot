# -*- coding=utf-8

# access_token 周期刷新的时间，单位为ms
RefreshPeriod = 1000 * 3600

# 公众平台的配置信息, 多个公众平台以列表形式往后追加
MediaPlatforms = [
    {
        'name': u'mp_test_plat',
        'desc': u'公众号测试平台',
        'appid': 'xxxx', # 需要自己配置
        'appsecret': 'xxxx', # 需要自己配置
    },
]
