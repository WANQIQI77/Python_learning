'''
2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
'''


def read_file():
    list_line = []
    with open("data\\input.txt", 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                return list_line
            list_line.append(line)


def getInfo(list_input):
    j = 1
    for i in list_input:
        print("第{}行：{}".format(j, i))
        j = j + 1


if __name__ == "__main__":
    getInfo(read_file())
