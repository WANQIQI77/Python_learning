# -*- coding: utf-8 -*-            
# @Time : 2022/11/2 16:31
# @Author:One77
# @FileName: Q4.py
# @Software: PyCharm

'''
4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''

import os

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
for i in list1:
    with open("img\\" + str(i) + ".png", 'w'):
        pass

files = os.listdir("img")
for f in files:
    portion = os.path.splitext(f)
    if portion[1] == ".png":
        oldname = portion[0] + ".png"
        newname = portion[0] + ".jpg"
        os.rename("img\\" + oldname, "img\\" + newname)
