name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")

info = '''
--- info of {_name}
Name：{_name}
Age：{_age}
Skill：{_skill}
alary：{_salary}
'''.format(_name=name, _age=age, _skill=skill, _salary=salary)

print(info)