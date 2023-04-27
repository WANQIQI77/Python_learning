'''
9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
import random
def Sort(sort_list):
    sort_list.sort()
if __name__=="__main__":
    list=[random.randint(0,100) for i in range(10)]
    Sort(list)
    print(list)