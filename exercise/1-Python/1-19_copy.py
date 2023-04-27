'''
将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
     提示: 写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。
     还需要判断一下这个文件之前是否存在;
     读源文件的内容;
     创建目标文件;
     读到的内容,再写入到目标文件
'''
import os


def copy(file_1, file_2):
    folder = os.path.exists(file_1)
    if not folder:
        print('文件夹不存在，需要现在创建')
        with open(file_1, 'w', encoding='utf-8'):
            pass
    with open(file_2,'w',encoding='utf-8') as file_to:
        file_from = open(file_1, 'r', encoding='utf-8')
        file_to.write(file_from.read())
        file_from.close()



if __name__ == "__main__":
    file_1 = 'data\\from.txt'
    file_2 = 'data2\\to.txt'
    copy(file_1, file_2)
