# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 18:19
# @software:pycharm

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
    return a


for i in range(10):
    print(Fibonacci(i), end=' ')
