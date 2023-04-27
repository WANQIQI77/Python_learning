'''
 4 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
'''


def count(str):
    digit_num = 0
    letter_num = 0
    other_num = 0
    space_num = 0
    for i in str:
        if i.isdigit():
            digit_num = digit_num + 1
        elif i.isalnum():
            letter_num = letter_num + 1
        elif i.isspace():
            space_num = space_num + 1
        else:
            other_num = other_num + 1
    print("字母个数：", letter_num)
    print("数字个数：", digit_num)
    print("空格个数：", space_num)
    print("其他字符个数：", other_num)
    return digit_num, letter_num, space_num, other_num


if __name__ == "__main__":
    str = 'jsdhj 14334   /////'
    count(str)
