'''
1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''


def myInput():
    list_line = []
    print("请输入任意行信息，当输入空行时结束")
    while True:
        line = input()
        if not line:
            return list_line
        list_line.append(line)


def write_file(list_line):
    with open("data\\input.txt", "w", encoding='utf-8') as f:
        for i in list_line:
            f.write(i)
            f.write('\n')


if __name__ == "__main__":
    list1 = myInput()
    write_file(list1)
