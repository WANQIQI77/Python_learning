'''
3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成;
'''

import random

def odd_number(list1):
    list2=[]
    for i in list1:
        if i%2!=0:
            list2.append(i)
    return list2
if __name__ == "__main__":
    list1 = [random.randint(0, 100) for i in range(10)]
    print(list1)
    print(odd_number(list1))

