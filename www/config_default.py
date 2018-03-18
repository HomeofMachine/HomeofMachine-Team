#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Mosan'

'''
符合本地开发环境的默认配置
'''

#配置文件的数据类型是字典
configs = {
    'debug': True,
    'db':  {
        'host': '127.0.0.1', 
        'port': 3306, 
        'user': 'root', 
        'password': 'mysqlmima1995', 
        'db': 'jxzj'
    },
    'session':  {
        'secret':  'Jxzj'
    }
}
