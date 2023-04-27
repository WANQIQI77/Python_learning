# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 12:59
'''
4  判断用户输入的年份是否为闰年
'''

year = int(input('请输入要判断的年份'))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400) == 0:
    print("{}年是闰年".format(year))
else:
    print("{}年不是闰年".format(year))
