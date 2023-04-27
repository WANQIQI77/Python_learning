# -*- coding: utf-8 -*-            
# @Time : 2022/11/4 17:21
# @Author:One77
# @FileName: Q6.py
# @Software: PyCharm
'''
6 有两个列表
 list1 = [aa，11, 22, 33] ；lsit2 = [bb，22, 33, 44]
        请找出它们中相同的元素；
'''
list1 = ['aa', 11, 22, 33]
list2 = ['bb', 22, 33, 44]

set1 = set(list1)
set2 = set(list2)

set3 = set1 & set2
print(set3)
