#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MoSan'

'''
async web 应用
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs

import orm
from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME

def init_jinja2(app, **kw): # 初始化jinja2引擎函数
    logging.info('init jinja2...') #logging库信息显示方法info
    options = dict( #定义选项字典;kw.get方法的功能是若有则获取，没有则按第二个参数生成
        autoescape = kw.get('autoescape', True), #获取自动撤离参数
        block_start_string = kw.get('block_start_string', '{%'), #获取块起始字符串
        block_end_string = kw.get('block_end_string', '%}'), #获取块结束字符串
        variable_start_string = kw.get('variable_start_string', '{{'), #获取变量起始字符串
        variable_end_string = kw.get('variable_end_string', '}}'), #获取变量结束字符串
        auto_reload = kw.get('auto_reload', True) #获取自动重载参数
    )
    path = kw.get('path', None) #获取路径参数
    if path is None: #若路径为空
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') #重新加入路径
    logging.info('set jinja2 template path: %s' % path) #显示登录信息：设置引擎模板路径
    env = Environment(loader=FileSystemLoader(path), **options) #jinja2库函数FileSystemLoader传入路径参数，再传入Environment库函数生成环境实例
    filters = kw.get('filters', None) #获取过滤器参数
    if filters is not None: #若过滤器为非空
        for name, f in filters.items(): #环境实例加入过滤参数
            env.filters[name] = f
    app['__templating__'] = env #将app的内部参数templating设置为env实例

@asyncio.coroutine #python的@语法，放在函数的定义处，此处表示：logger_factory = asyncio.coroutine(logger_factory);把定义后的函数作为参数传送给@后的函数
def logger_factory(app, handler): #日志记录器工厂协程函数
    @asyncio.coroutine
    def logger(request): #日志记录器协程函数
        logging.info('Request: %s %s' % (request.method, request.path)) #日志显示请求方法与请求路径信息
        # yield from asyncio.sleep(0.3)
        return (yield from handler(request)) #使用另一协程获取对请求的处理结果并返回
    return logger #返回值为函数

@asyncio.coroutine
def auth_factory(app, handler): #认证工厂协程函数
    @asyncio.coroutine
    def auth(request): #认证协程函数，传入请求
        logging.info('check user: %s %s' % (request.method, request.path)) #显示登录信息检查用户：来自请求方法，请求路径
        request.__user__ = None #请求的内部用户变量设置为空
        cookie_str = request.cookies.get(COOKIE_NAME) #尝试从请求的cookies中获取cookie名（若存在）
        if cookie_str: #若该cookie信息存在
            user = yield from cookie2user(cookie_str) #调用协程将cookie转化为用户信息
            if user: #若用户信息存在
                logging.info('set current user: %s' % user.email) #显示日志：设置当前用户为：用户邮件
                request.__user__ = user #将请求内部用户变量设置为该用户
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin): #若请求路径以管理为开始并且请求内部用户为空或者不是管理员用户
            return web.HTTPFound('/signin') #返回web库方法HTTPFound，参数为登录页url
        return (yield from handler(request)) #返回调用协程对请求的处理结果
    return auth #返回认证函数

@asyncio.coroutine
def data_factory(app, handler): #数据工厂协程
    @asyncio.coroutine
    def parse_data(request): #解析数据协程
        if request.method == 'POST': #若请求方法为post
            if request.content_type.startswith('application/json'): #若请求内容类型以application/json为开始
                request.__data__ = yield from request.json() #将请求数据设置为协程对request的json实例
                logging.info('request json: %s' % str(request.__data__)) #显示日志信息：请求json数据
            elif request.content_type.startswith('application/x-www-form-urlencoded'): #又若请求内容类型是应用/x-www格式的url编码
                request.__data__ = yield from request.post() #将请求数据设置为协程获得的请求post实例
                logging.info('request form: %s' % str(request.__data__)) #显示日志 信息请求类型为：
        return (yield from handler(request)) #返回 协程处理请求的结果
    return parse_data #返回解析数据函数

@asyncio.coroutine
def response_factory(app, handler): #响应生成器协程
    @asyncio.coroutine
    def response(request): #响应协程
        logging.info('Response handler...') #日志显示：响应处理器
        r = yield from handler(request) #获取协程处理请求的结果
        if isinstance(r, web.StreamResponse): #判断是否为web库的流响应实例
            return r #若是，则返回该实例
        if isinstance(r, bytes): #判断是否为字节型实例，若是则
            resp = web.Response(body=r) #获取body参数为r的响应 实例
            resp.content_type = 'application/octet-stream' #将该响应实例的内容类型该设置为应用/octet流
            return resp #返回该响应实例
        if isinstance(r, str): #若是字符型实例
            if r.startswith('redirect:'): #若该实例以重定位起始
                return web.HTTPFound(r[9:]) #返回参数为该实例的第九个元素之后为参数的web库HTTPFound实例
            resp = web.Response(body=r.encode('utf-8')) #获取body参数为r实例编码为utf-的web 响应实例
            resp.content_type = 'text/html;charset=utf-8' #将该实例类型设置为文本/html;字符设置 为utf8
            return resp #返回该实例
        if isinstance(r, dict): #若该实例为字典类型
            template = r.get('__template__') #获得该实例的内部模板参数
            if template is None:#若该模板参数为空
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')) #获得body参数为json缩进以及设置参数的r实例的web库响应实例
                resp.content_type = 'application/json;charset=utf-8' #设置响应实例的内容类型
                return resp #返回 响应实例
            else: #若该模板不为空
                r['__user__'] = request.__user__ #r实例的内部用户变量设置为请求的内部用户
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8')) #获取设置参数的web库响应实例
                resp.content_type = 'text/html;charset=utf-8' #设置返回实例的内容类型
                return resp 
        if isinstance(r, int) and t >= 100 and t < 600: #若该实例为int型且其值大于100小于600
            return web.Response(t) #返回参数为t的web响应实例
        if isinstance(r, tuple) and len(r) == 2: #若参数类型是tuple且长度为2
            t, m = r #获取r的两个元素
            if isinstance(t, int) and t >= 100 and t < 600: #若第一个元素为int型且大于100小于600
                return web.Response(t, str(m)) #返回参数为t和字符型m的网页响应实例
        # default: 
        resp = web.Response(body=str(r).encode('utf-8')) #获取body参数为实例r字节型utf-8编码的web 响应实例
        resp.content_type = 'text/plain;charset=utf-8' #设置响应内容类型
        return resp
    return response

def datetime_filter(t): #日期时间过滤函数
    delta = int(time.time() - t) #获取时间间隔
    if delta < 60: 
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

@asyncio.coroutine
def init(loop): #初始化函数
    yield from orm.create_pool(loop=loop, **configs.db) #调用协程创建数据库连接池
    app = web.Application(loop=loop, middlewares=[
        logger_factory, auth_factory, response_factory
    ]) #web库方法Application传入循环实例，以获取web app实例
    init_jinja2(app, filters=dict(datetime=datetime_filter)) #自写函数传入app实例，初始化jinja2模板引擎
    add_routes(app, 'handlers') #增加路径
    add_static(app)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop() #获取事件循环实例
loop.run_until_complete(init(loop)) #放入初始化的循环实例，并运行直至完成
loop.run_forever() #持续运行
