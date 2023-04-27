name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")

info='''
---info of {0}---
Name:{0}
Age:{1}
skill:{2}
Salary:{3}
'''.format(name,age,skill,salary)
print(info)