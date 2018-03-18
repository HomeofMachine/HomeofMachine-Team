#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

__author__ = 'Mosan'

'''
为了解决每次修改脚本都需要杀掉服务器进程再重启的繁琐步骤
这里用脚本实现自动检查脚本变化并重启服务器进程
'''

#加载三方库
import sys, os, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#定义日志输出函数
def log(s):
    print("[Monitor] %s" % s)

#定义文件系统事件处理类
class MyFileSystemEventHander(FileSystemEventHandler):
# 定义类初始化方法    
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

# 定义类事件
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log("Python source code %s has changed:" % event.src_path)
            self.restart()

#声明命令和进程变量
command = ['echo', 'ok'] #["echo", "ok"]
process = None

#定义杀进程方法
def kill_process():
    global  process
    if process:
        log("Kill process [%s]" % process.pid)
        process.kill()
        process.wait()
        log("Process ended with code %s" % process.returncode)
        process = None

#定义启动进程方法
def start_process():
    global process, command
    log("Start process %s" % ' '.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

#定义重启进程方法
def restart_process():
    kill_process()
    start_process()
#定义启动监视方法
def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive=True)
    observer.start()
    log("Watching direction %s..." % path)
    start_process() #缺了该命令则不会执行app.py脚本
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
	    observer.stop()
    observer.join()

#模块加载/运行状态判断
if __name__ == '__main__':
    argv = sys.argv[1:] #从当前运行的脚本中获取当前需要监控的脚本
    if not argv:
        print("Please enter:./pymonitor.py your_script_name.py")
        exit(0)
    if argv[0] != 'python3':
        argv.insert(0, 'python3')
    command = argv
    path = os.path.abspath('.') #获取当前目录的绝对路径
    start_watch(path, None) #test
