'''
8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
'''

from collections import Counter


def get_max_char(str):
    count = Counter(str)
    print(count)
    #以为count现在是一个对象，利用他的属性--count.values()取出其中的值
    count_list = list(count.values())
    print(count_list)
    max_value = max(count_list)
    max_list = []
    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    # max_list = sorted(max_list) #加这个排序的原因是，如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母
    # return max_list[0]
    return max_list


str1 = 'abcdacdgjkdka'
print(get_max_char(str1))


