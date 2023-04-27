# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 15:01
'''
设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败
'''
import random
flag=10
a = random.randint(0,100)
print(a)
while 1:
    if flag==0:
        print('猜测失败')
        break
    x=int(input('请输入您猜测的数字'))
    flag=flag-1
    if(x==a):
       print('猜测正确')
       break
    else:
       continue

