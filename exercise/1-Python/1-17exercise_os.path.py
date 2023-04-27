import os

#打印当前文件路径的两种方法
file = os.getcwd()
print(file)
print(os.path.abspath(file))

# 指定目录下创建目录
os.mkdir(file+"//test")

#列出指定目录下的所有文件
for filename in os.listdir(file):
    print(filename)

