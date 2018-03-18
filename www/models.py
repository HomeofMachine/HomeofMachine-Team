#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ ='Mosan'

'''
创建数据库表的model实例对象
'''

from orm import Model, StringField, BooleanField, FloatField, TextField
import time, uuid
#uuid即是Universal Unique IDendifier全局唯一 标识符可通过多种方式来保证ID的唯一性

#生成唯一的ID
def next_id():
    return '%015d%s000' % (int(time.time() *1000), uuid.uuid4().hex) #uuid4是基于随机数的方式

#生成User即用户信息模型
'''
def User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)') #调用函数为何不带()
    email = StringField(ddl='varchar(50)') #参数若为定义时设置的默认值，则不需要传入 
    name = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    image = StringField(ddl='varchar(500)') #TextField和StringField的区别在于文本和字符串（容量大小）;这里同时限制了图片的大小为500的字符?
    created_at = FloatField(default=time.time)
问题可能出在顺序
'''


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

