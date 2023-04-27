# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 14:57


for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, i * j), end=' ')
    print()

