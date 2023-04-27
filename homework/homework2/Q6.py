'''
6  定义一个函数, 打印输出n以内的斐波那契数列
'''


def fib(n):
    a = 0
    b = 1
    print(1, end=' ')
    print(b, end=' ')
    while ((b + a + b) < n):
        a = b
        b = a + b
        print(b, end=' ')


if __name__ == "__main__":
    n = 100
    fib(n)
