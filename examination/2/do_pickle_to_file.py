# -*- coding: utf-8 -*-            
# @Time : 2022/11/11 17:51
# @Author:One77
# @FileName: do_pickle_to_file.py
# @Software: PyCharm
'''
题目3(文件名：do_pickle_to_file.py）：利用pickle模块，将数据序列化保存到文件--2.5'
利用字典解析式，生成记录一组学生2门课的成绩的字典列表，
将这个字典列表序列化以后，保存到一个文件中（列表中的每一个元素，保存为文件中的一行）；
'''
import pickle
import random


def save(mylist):
    with open ('pickle.pkl','wb') as file:
        pickle.dump(mylist,file)


def dict_list(n=2):
    ress=[]
    keys=['stuName','English','Math']
    for _ in range(n):
        dic={keys[i]:random.randint(60,100) for i in range(1,3)}
        dic[keys[0]] = name(random.randint(3,6))
        print(dic)
        ress.append(dic)
    print(ress)
    return ress

def name(n):
    letter='gazw'
    name=''
    for i in range(n):
        name+=random.choice(letter)


    print(name)
    return name




if __name__=="__main__":
    mylist=dict_list()
    save(mylist)