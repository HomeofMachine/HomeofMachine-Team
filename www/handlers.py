#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MoSan'

' url 处理函数 '

import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def check_admin(request): #检查管理权限函数 
    if request.__user__ is None or not request.__user__.admin: #若请求报文中没有用户项或不是管理员用户 
        raise APIPermissionError() #raise关键字用于引发异常

def get_page_index(page_str): #获取页数函数 
    p = 1 #初始化变量 
    try:
        p = int(page_str) #将包含字符型页数转换为数字
    except ValueError as e: #若发生值错误，则什么都不做（返回默认值1）
        pass
    if p < 1:
        p = 1
    return p

def user2cookie(user, max_age): #特定用户产生cookie函数
    '''
    Generate cookie str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age)) #根据当前时间与最大页数生成字符串，即cookie有效时间
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY) #综合用户id、用户密码、字符串以及cookie键生成字符串
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()] #使用哈希sha1型加密方式生成列表
    return '-'.join(L) #返回列表的字符型

def text2html(text): #文本转换为html函数
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@asyncio.coroutine
def cookie2user(cookie_str): #将cookie转化为用户信息的协程函数
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str: #若为空直接返回空
        return None
    try:
        L = cookie_str.split('-') #按照之前生成cookie的格式分解
        if len(L) != 3: #若没有三个横杠即四个字符串即返回空
            return None
        uid, expires, sha1 = L #分别拿出前三个字符串。另外python里用空格而不用tab缩进否则会报错
        if int(expires) < time.time(): #若比当前时间小，表示cookie失效
            return None
        user = yield from User.find(uid) #中断该函数执行并在数据库中检查该用户的存在
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest(): #若加密方式不是sha1表示是伪造的cookie
            logging.info('invalid sha1') #报错非法sha1
            return None
        user.passwd = '******'
        return user #返回user实例表明登录成功
    except Exception as e:
        logging.exception(e)
        return None

@get('/') #对get型url的处理函数，是一个装饰器
def index(*, page='1'):
        return { #返回写好的模板以及填入新的内容
        '__template__': 'index.html',
        #'page': page,
        #'blogs': blogs
    }


'''
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    page = Page(num)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
'''

@get('/blog/{id}')
def get_blog(id):
    blog = yield from Blog.find(id)
    comments = yield from Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }

@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }

@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }

#新增验证码登录
@get('/getcode')
def getcode():
    pass 

@post('/api/authenticate') #post型URL处理函数：登录信息验证
def authenticate(*, email, passwd):
    if not email: #若邮件空
        raise APIValueError('email', 'Invalid email.') #产生错误
    if not passwd: #若密码空
        raise APIValueError('passwd', 'Invalid password.')
    users = yield from User.findAll('email=?', [email]) #中断并按邮件从数据库中查找用户
    if len(users) == 0: #若返回空值则报错
        raise APIValueError('email', 'Email not exist.')
    user = users[0] #查询成功，用户则为users实例的第一个元素
    # check passwd:
    sha1 = hashlib.sha1() #sha1对象
    sha1.update(user.id.encode('utf-8')) 
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest(): #若生成密码加密值不一致则密码错误
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response() #网页响应对象
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True) #对其生成cookie
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/signout') #定义登出函数装饰器
def signout(request):
    referer = request.headers.get('Referer') #获取请求头部的参考字段
    r = web.HTTPFound(referer or '/') #找到现存的web对象
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True) #设置器cookie状态为登出
    logging.info('user signed out.') #提示信息
    return r

@get('/manage/')
def manage():
    return 'redirect:/manage/comments'

@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }

@get('/manage/blogs/edit')
def manage_edit_blog(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id
    }

@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

#测试函数
@get('/test1')
def test1(*, page='2'):
	return {
		'__template__': 'manage_users.html',
		'page_index': get_page_index(page)
	}
@get('/test2')
def test2():
	return {
		
"hello,world"                       		
	}

@get('/api/comments')
def api_comments(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Comment.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = yield from Comment.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

@post('/api/blogs/{id}/comments')
def api_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = yield from Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.name, user_image=user.image, content=content.strip())
    yield from comment.save()
    return comment

@post('/api/comments/{id}/delete')
def api_delete_comments(id, request):
    check_admin(request)
    c = yield from Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(id=id)

@get('/api/users')
def api_get_users(*, page='1'):
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = yield from User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p, users=users)

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$') #定义邮箱输入格式
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$') #定义密码输入格式

@post('/api/users')
def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('passwd')
    users = yield from User.findAll('email=?', [email]) #中断去数据库检查是否已注册
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id() #如检验成功生成新用户的id
    sha1_passwd = '%s:%s' % (uid, passwd) #结合id对用户密码加密
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())#填写数据库的user表
    yield from user.save() #中断调用协程进行高保存
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/api/blogs')
def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)

@get('/api/blogs/{id}')
def api_get_blog(*, id):
    blog = yield from Blog.find(id)
    return blog

@post('/api/blogs')
def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip())
    yield from blog.save()
    return blog

@post('/api/blogs/{id}')
def api_update_blog(id, request, *, name, summary, content):
    check_admin(request)
    blog = yield from Blog.find(id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    yield from blog.update()
    return blog

@post('/api/blogs/{id}/delete')
def api_delete_blog(request, *, id):
    check_admin(request)
    blog = yield from Blog.find(id)
    yield from blog.remove()
    return dict(id=id)
