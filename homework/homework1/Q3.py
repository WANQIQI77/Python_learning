# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 12:36
'''
3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
'''
list1 = ['apple', 'banana']
list2 = [1, 2, 3, 4, 5, 6, 7, 'apple']
set1 = set(list1)
set2 = set(list2)
set3 = set1 & set2
list3 = list(set3)
print(list3)
