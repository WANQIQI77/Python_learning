# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 18:23
# @software:pycharm
import random


def is_odd(n):
    return n % 2 == 1


list1 = [random.randint(1, 20) for _ in range(10)]
print(list1)

list2 = filter(lambda x: x % 2, list1)
print(list(list2))
