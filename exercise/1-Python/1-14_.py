# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 18:38
# @software:pycharm

def printinfoList( **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(vardict)

def printinfoDict( *vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(vardict)

# 调用printinfo 函数
# printinfo(70, 60, 50,80)
printinfoList(a=2, b=3)
printinfoDict(2, 3)
