#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
配置文件管理
'''

__author__ = 'MoSan'

import config_default

class Dict(dict): #继承dict类
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw): #仅当定义类内方法时需加self
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override): #合并配置文件函数，实现快速开发部署
    r = {}
    for k, v in defaults.items(): #使用字典的item()方法使键值分离
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d): 
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
