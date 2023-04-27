'''
10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
'''


def calculate(a, b):
    print("a+b=", a + b)
    print("a-b=", a - b)
    print("a*b=", a * b)
    if b == 0:
        print("0不能做除数")
    else:
        print("a/b=", a / b)


if __name__ == "__main__":
    a = int(input("第一个数："))
    b = int(input("第二个数："))
    calculate(a, b)
