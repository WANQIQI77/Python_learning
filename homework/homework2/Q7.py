'''
7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
    A---成绩>=90;
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''
import random


def Degree(student_score):
    for key, val in student_score.items():
        if val >= 90:
            print(key + "  A")
        elif val >= 80 and val < 90:
            print(key + "  B")
        elif val >= 70 and val < 80:
            print(key + '  C')
        else:
            print(key + "  C")


if __name__ == "__main__":
    student_score = {}
    for i in range(1, 21):
        name = 'stu' + str(i)
        score = random.randint(0, 101)
        student_score[name] = score
    print(student_score)
    Degree(student_score)
