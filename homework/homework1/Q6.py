# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 14:51

mylist = [0, 1]
while 1:
    a = mylist[-1] + mylist[-2]
    if a>100:
        break
    else:
        mylist.append(a)
print(mylist)
