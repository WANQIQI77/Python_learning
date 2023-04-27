# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 15:01
'''
给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
提示：可以用字典来统计：key 是单词，value 是单词出现次数；
先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 如果这个单词没出现过，就直接 插入这个单词及value 为 1 到 字典中；
'''
a = 'This book contains a fairy tale,a story about many things.First of all,Innocence of Childhood and love.'
a = a.replace(',', ' ')
a = a.replace('.', ' ')
print(a)
list1 = a.split()

print(list1)
set1 = set(list1)
list2 = list(set1)
listva = [0 for i in range(len(list2))]

dict1 = zip(list2, listva)
dict2 = dict(dict1)

for j in dict2.keys():
    for i in list1:
        if j == i:
            dict2[j] = dict2[j] + 1
print(dict2)
