#创建元组
mytup1 = (1,2,3,4,5,6,'sss')
print(mytup1[0:3])

#元组连接组合
mytup2=mytup1+('wqq',)
print(mytup2)

listgrade=[]
for i in range(5):
    x = input("输入成绩：")
    listgrade.append(x)
mytupGrade=tuple(listgrade)
print(mytupGrade)
print(max(mytupGrade))

