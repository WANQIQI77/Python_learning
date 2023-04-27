# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 16:17
import random


b = [random.randint(1, 10) for _ in range(10)]
for i in b:
    print(i)
print('--------------')
for i in b:
    if i % 2 == 0:
        print(i)


