'''
练习1:
      定义一个高阶函数, 实现加,减,乘,除计算器功能;
      highfunc(a ,b  ,func)
'''
def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def reduc(a,b):
    return a-b
def div(a,b):
    return a/b

def highfunc(a,b,func):
    return func(a,b)

print(highfunc(10,10,add))