#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Mosan'

'''
用以简化配置文件的读取
'''

import config_default

#定义支持x.y风格存取的字典类
class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribution %s" % key)
    def __setattr__(self, key, value):
        self[key] = value

#定义配置文件合并方法,用递归对字典解包
def merge(default, override):
    r = {}
    for k, v in default.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v 
    return r
            
#定义方法实现：将多层字典转化为单层字典
def toDict(d):
    D = Dict() #与dict的区别在哪
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs
try:
    import config_override
    configs = merge(configs, config_override.configs) #这里的merge不是python的内置函数，但是也不用实现,因为配置的时候？环境会有实现
except ImportError:
    pass 
configs = toDict(configs)
