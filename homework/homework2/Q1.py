'''
1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
'''


def find_length(x):
    return len(x)


if __name__ == "__main__":
    mydict = {1: 'qq', 2: 'zz'}
    mylist = [1, 2, 3, 4]
    mytuple = (1, 2, 4, 5)
    print(find_length(mydict))
    print(find_length(mylist))
    print(find_length(mytuple))