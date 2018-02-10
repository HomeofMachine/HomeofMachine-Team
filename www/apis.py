#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mosan'

'''
JSON API定义
'''

import json, logging, inspect, functools

class Page(object): #定义Page类用以展示页面
    '''
    Page object for display pages.
    '''

    def __init__(self, item_count, page_index=1, page_size=10): #初始化函数
        '''
        Init Pagination by item_count, page_index and page_size.

        >>> p1 = Page(100, 1)
        >>> p1.page_count
        10
        >>> p1.offset
        0
        >>> p1.limit
        10
        >>> p2 = Page(90, 9, 10)
        >>> p2.page_count
        9
        >>> p2.offset
        80
        >>> p2.limit
        10
        >>> p3 = Page(91, 10, 10)
        >>> p3.page_count
        10
        >>> p3.offset
        90
        >>> p3.limit
        10
        '''
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index - 1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1

    def __str__(self): #
        return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)

    __repr__ = __str__

class APIError(Exception): #定义API调用错误类，基类包含错误(必须)，数据(可选)、消息(可选)
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''
    def __init__(self, error, data='', message=''): #初始化函数
        super(APIError, self).__init__(message) #super用以解决多重继承，可以直接调用父类名;
        self.message = message

class APIValueError(APIError): #API值错误类
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError): #API资源未找到错误类
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)

if __name__=='__main__': #当模块正在运行时其name就是main，即当模块正在运行时以下代码块会被执行;若仅是被加载则不会执行
    import doctest
    doctest.testmod()
