

mystring='ksaljdl kjl kkk'

find_str=input("请输入要查找的字符串：")

if find_str in mystring:
    print("%s在字符串中"%find_str)
else:
    print('%s不在字符串中'%find_str)
mystring2=mystring.replace("kjl", "love")
print(mystring2)
print(len(mystring))