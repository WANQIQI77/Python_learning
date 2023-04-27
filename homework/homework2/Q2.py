'''
2 编写一个函数,接收n个数字，求这些参数数字的和;
'''

def sum(n):
    sum=0
    for i in range(n):
        x=int(input())
        sum=sum+x
    return sum
if __name__=="__main__":
    x=int(input("请输入求和数字的数量："))
    print(sum(x))
