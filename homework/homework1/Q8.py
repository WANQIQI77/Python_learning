# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 15:01
'''
设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
提示：可以组合使用我们的序列数据类型；
'''

import random

emp = [[f'00{i}', f'name{i},', random.randint(1, 5), random.randint(1000, 10000)] for i in range(10)]
print(emp)


emp.sort(key=lambda l: l[3], reverse=True)
print(emp)

