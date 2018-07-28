# WeTokenBot

## 背景

公司管理的公众号越来越多，每个公众号的各种服务又依赖于access_token，每个access_token都只有2个小时的有效期，需要定时刷新。

需要有一个服务来专门托管刷新access_token的任务。于是就有了这个项目。

## 功能概要

1. webapi 提供查看当前管理了哪些公众号
2. api端需要能快速的获取到token信息
3. 提供主动刷新的接口
4. 定时刷新token

## 模块依赖

- tornado.web 提供webapi支持
- tornado.ioloop.PeriodicCallback 提供定时刷新支持

```bash
pip install -r requirements.txt
```

## 快速开始

配置公众号信息

