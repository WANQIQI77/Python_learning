# -*- coding: utf-8 -*-            
# @Time : 2022/11/2 16:22
# @Author:One77
# @FileName: Q3.py
# @Software: PyCharm

'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数);
然后按照分数从高到低进行排序输出
'''

with open("data\\student.txt", "r", encoding='utf-8') as f_read:
    read = f_read.read()

mylist = read.split()

mydict = {}
listall = []
listsmall = []

for i in range(4, 32, 3):
    listsmall = [mylist[i - 1], mylist[i], mylist[i + 1]]
    list2 = listsmall
    listall.append(list2)

listall.sort(key=lambda x: x[2],reverse=True)

with open("data\\stu_write.txt", "w", encoding='utf-8') as f_write:
    f_write.write("姓名    学号     分数\n")
    for i in range(10):
        str = '    '.join(listall[i])
        print(str)
        f_write.write(str + '\n')
