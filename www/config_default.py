#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
默认配置，即本地开发配置
'''

__author__ = 'Mosan'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'mysqlmima1995',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
