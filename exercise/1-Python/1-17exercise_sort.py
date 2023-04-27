import os

'''
练习:   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
            姓名      学号      分数
            张三      101       78
            李四      102       87
            王五      103       83
'''

'''
希望得到：
mydict={
        '101':['张三','78']
        .......
        }
'''
with open("data\\read.txt", "r", encoding='utf-8') as f_read:
    read = f_read.read()
mylist = read.split()
print(mylist)
mydict = {}
listall = []
listsmall = []
for i in range(4, 11, 3):
    listsmall = [mylist[i - 1], mylist[i], mylist[i + 1]]
    print(listsmall)
    list2 = listsmall
    listall.append(list2)
print(listall)
listall.sort(key=lambda x: x[2])
print(listall)

with open("data\\write.txt", "w", encoding='utf-8') as f_write:
    f_write.write("姓名    学号     分数\n")
    for i in range(3):
        str='    '.join(listall[i])
        print(str)
        f_write.write(str+'\n')

