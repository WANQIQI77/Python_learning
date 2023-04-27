f1 = open("test\\b", "r", encoding='UTF-8')
#print(f1.read())
  #如果文件很大，这样容易爆内存

for line in f1.readlines():
    print(line.strip())