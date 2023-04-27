import os

f = open("test.txt", "w", encoding='UTF-8')

f.write("pyhton66\n");
f.write("999\n")

f1 = open("test\\a.txt", "w", encoding='UTF-8')
f1.write("同级目录写入")

f2 = open("..\\b.txt", "w", encoding='UTF-8')
f2.write("上级目录写入")

f.close()
f1.close()
f2.close()
