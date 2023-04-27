'''
练习:  定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;
'''
import time


def RunDiag(func):
    def inner(a, b):
        func(a, b)
        print(time.time())

    return inner


@RunDiag
def add(a, b):
    print(a + b)


add(3, 4)
add(5, 6)
