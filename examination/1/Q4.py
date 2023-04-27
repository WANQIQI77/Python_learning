# -*- coding: utf-8 -*-            
# @Time : 2022/11/4 17:14
# @Author:One77
# @FileName: Q4.py
# @Software: PyCharm
'''
 输入三个整数x,y,z，请把这三个数由小到大输出
'''

list1 = []
for i in range(3):
    a = int(input())
    list1.append(a)
list2 = sorted(list1)
print(list2)
