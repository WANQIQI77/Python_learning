# -*- coding: utf-8 -*-            
# @Time : 2022/11/11 17:41
# @Author:One77
# @FileName: do_dict_input.py
# @Software: PyCharm
'''
题目2（文件名：do_dict_input.py）：字典列表初始化--2.5'
     有一个字典数组，存放了一个小组N个同学的信息；参考结构如下：
      [
          {
    "name":"marry",
    "city":"北京",
    "age":"20"
},
{
    "name":"tom",
    "city":"上海",
    "age":"20"
            }
        ......
    ]
    A  请从键盘输入数据，初始化这N个同学的信息；
    B  按照年龄从大到小的顺序，输出这N个同学的信息；
'''


def getInfo():
    list_all_stu = []

    n = int(input("请输入学生数量："))
    for i in range(n):
        dict_stu = {}
        name = input("姓名：")
        city = input("城市：")
        age = input("年龄：")
        dict_stu['name'] = name
        dict_stu['city'] = city
        dict_stu['age'] = age
        list_all_stu.append(dict_stu)
    return list_all_stu


if __name__ == "__main__":
    list_stu = []
    list_stu = getInfo()
    print("-----排序前---------")
    print(list_stu)
    print('------排序后---------')
    list_stu.sort(key=lambda x: x['age'])
    print(list_stu)
