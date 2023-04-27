# -*- coding: utf-8 -*-            
# @Time : 2022/11/11 17:30
# @Author:One77
# @FileName: do_list_input.py
# @Software: PyCharm
'''
题目1（文件名：do_list_input.py）：列表初始化-2.5'
从键盘上输入一组数据(要求一行输入)，用空格隔开；
并将这一组数据（如果其中的数据能转换成整数，请转换成整数）存放到一个列表中；并打印输出列表的值；
'''


def to_Int(str):
    list1 = str.split(" ")
    list_int=[]
    for i in list1:
        if(i.isdigit()):
            list_int.append(int(i))
    return list_int



if __name__ == "__main__":
    str = input("输入一行数据，用空格隔开")
    list_int = []
    list_int = to_Int(str)
    print(list_int)
