# WeTokenBot

## 背景

公司管理的公众号越来越多，每个公众号的各种服务又依赖于access_token，每个access_token都只有2个小时的有效期，需要定时刷新。

需要有一个服务来专门托管刷新access_token的任务。于是就有了这个项目。

## 功能概要

1. webapi 提供查看当前管理了哪些公众号（未实现）
2. api端需要能快速的获取到token信息
3. 提供主动刷新token的接口（未实现）
4. 定时刷新token

## 模块依赖

- tornado.web 提供webapi支持
- tornado.ioloop.PeriodicCallback 提供定时刷新支持

```bash
pip install -r requirements.txt
```

## 快速开始

### 编辑config.py

配置公众号信息，修改MediaPlatforms里面的内容，多个平台以列表形式往后添加
``` python
MediaPlatforms = [
    {
        'name': 'mp_test_plat',
        'desc': u'公众号测试平台',
        'appid': 'xxxx', # 需要自己配置
        'appsecret': 'xxxx', # 需要自己配置
    },
]
```

### 启动服务

``` bash
cd wetokenbot
python run.py
```

### 通过webapi获得token信息

``` bash
# name 对应config.py里面的name字段
curl 'http://127.0.0.1:8888/token?name=xxxx'
```
