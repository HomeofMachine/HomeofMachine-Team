#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Mosan'

'''
处理web app运行过程中出现的Error
比如REST API中的错误处理
'''

import json, inspect, logging, functools

#定义page对象来直接展示错误信息页
class Page(object):
    #由item_count, page_index和page_size初始化分页
    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0) #item_count是否为0
        #若当前页码数大于页面数（实际有效页面数），则重置页面参数
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else: #否则直接由参数生成
            self.offset = self.page_size * (page_index -1) 
            self.limit = self.page_size
            self.page_index = page_index
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1
    #获取当前页面的属性值
    def __str__(self):
        return "item_count %s, page_count %s, page_index %s, page_size %s, offset %s, limit %s" %(self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)
    #将对象的属性以及形式整理为一个可以打印输出的形式，如上所定义，按照惯例用repr(object)调用
    __repr__ = __str__

#定义API调用错误基类,其包含错误（必须）， 数据和消息（可选）
class APIError(Exception):
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)#避免多种继承的时候依据继承链多次间接调用父类，而是直接调用父类,相当于这里执行了APIError.__init__()
        self.error = error
        self.data = data
        self.message = message

#表明API调用的值错误或者非法的类，需要额外传入数据说明表单错误的域
class APIValueError(APIError):
    def __init__(self, field, message=''): #为何不用传error
        super(APIValueError, self).__init__('value:invalid', field, message)

#表明资源未找到，需传入数据表名未找到的资源名称
class APIResourceNotFoundError(APIError):
    def __int__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:not found', field, message)
  
#表明所调用的API没有权限
class APIPermissionError(APIError):
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:denied', 'permission', message)

#判断模块状态:doctest定义了模块的测试框架,相当于在shell里一条条测试模块函数
if __name__ == '__main__':
    import doctest
    doctest.testmod()













