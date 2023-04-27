'''
5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
'''


def check_dict(dict1):
    dict2 = {}
    for (key, val) in dict1.items():
        if len(val) > 2:
            dict2[key] = val[0:2]
        else:
            dict2[key] = val
    return dict2


if __name__ == "__main__":
    mydict = {'1': (1, 2, 3, 'qq'), '2': (1, 2), '3': 'jjzzzz'}###value尽量不要用单个的int型，不能求长度
    dict2 = check_dict(mydict)
    print(dict2)
