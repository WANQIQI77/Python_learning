f1 = open("test\\a.txt", "r", encoding='UTF-8')
print(f1.read())

# f1 = open("test\\a.txt", "r")
# print(f1.read().decode('utf-8'))
##报错

f1.close()
