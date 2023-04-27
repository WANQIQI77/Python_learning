# -*- coding: utf-8 -*-            
# @Time : 2022/11/4 17:21
# @Author:One77
# @FileName: Q5.py
# @Software: PyCharm
'''
5 定义一个列表，通过键盘输入10个同学的姓名，
以及其Python成绩保存到该列表；
计算出平均分、最高分，最低分并打印；
'''

list1 = []
for i in range(10):
    name = input('name:')
    score = int(input('score:'))
    tu = [name, score]
    list1.append(tu)

sum = 0
for i in list1:
    sum += i[1]
ave = sum / len(list1)
print('平均值：', ave)

list2 = sorted(list1, key=(lambda x: x[1]))
print('最高分：', list2[9])
print('最低分：', list2[0])
