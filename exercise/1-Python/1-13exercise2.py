# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 18:11
# @soft:pycharm
import random


def printList(list):
    print(list)
    list.append('aaa')


if __name__ == "__main__":
    list = [random.randint(1, 10) for _ in range(10)]
    print("传参之前地址", id(list))
    printList(list)
    print("传参之后地址", id(list))
    print(list)
