# -*- coding: utf-8 -*-            
# @Time : 2022/11/11 17:53
# @Author:One77
# @FileName: do_decorator.py
# @Software: PyCharm
'''
题目4(文件名：do_decorator.py):装饰器使用--2.5'
定义一个记录日志到文件的函数（使用logging模块）；定义一个装饰器，当该装饰器装饰一个函数时，可以记录这个函数被调用了的事实（就是记录日志）和时间；
'''
import functools
import time
import logging


def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        func()
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
        # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
        logging.info('this is a loggging info message')
        logging.debug('this is a loggging debug message')
        logging.warning('this is loggging a warning message')
        logging.error('this is an loggging error message')
        logging.critical('this is a loggging critical message')

    return inner


@outer
def func():
    time.sleep(1)


func()
