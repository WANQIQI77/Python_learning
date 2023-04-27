# -*- coding: utf-8 -*-            
# @Time : 2022/11/11 17:53
# @Author:One77
# @FileName: do_file_score_sort.py
# @Software: PyCharm
'''
从键盘循环连续输入n个同学的姓名，语文，数学，外语成绩，保存到一个txt文件中；
备注：程序测试时，n请赋值为3和5分别测试；
'''


# 成绩数据录入并保存到文件
def input_grade(n):
    stu_list = []
    for i in range(n):
        stu = input("请输入第{}个同学的姓名及语数外成绩:".format(i + 1))
        stu_split = stu.split(" ")
        stu_list.append(stu_split)
    print(stu_list)
    with open('stu.txt', 'w', encoding='utf-8') as file:
        file.write('姓名\t语文\t英语\t数学\n')
        file.write('---------------------------------\n')
        for i in stu_list:
            file.write("{}\t{}\t{}\t{}\n".format(i[0], i[1], i[2], i[3]))




# 从文件读取成绩，并排序输出打印
def grade_sort(n):
    with open("stu.txt", "r", encoding='utf-8') as f_read:
        read = f_read.read()
    mylist = read.split()
    print(mylist)
    listall = []
    for i in range(5, 4 * n + 5, 4):
        listsmall = [mylist[i], mylist[i + 1], mylist[i + 2], mylist[i + 3]]
        print(listsmall)
        list2 = listsmall
        listall.append(list2)
    print(listall)
    for i in listall:
        i.append(int(i[1]) + int(i[2]) + int(i[3]))
    listall.sort(key=lambda x: x[4])
    print('排名\t姓名\t语文\t数学\t英语\t总分')
    print('-------------------------')
    for i in listall:
        j = 1
        print('{}\t{}\t{}\t{}\t{}\t{}\t'.format(j, i[0], i[1], i[2], i[3], i[4]))
        j=j+1


if __name__ == '__main__':
    n = 3
    input_grade(n)
    grade_sort(n)
