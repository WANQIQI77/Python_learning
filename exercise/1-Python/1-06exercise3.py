def addGrade(Grade):
    x=input("请输入添加的成绩")
    Grade.append(x)
    Grade.sort()
    return Grade
if __name__ == "__main__" :
    grade=[]
    for i in range(5):
        x=input("输入成绩：")
        grade.append(x)
    grade.sort()
    for i in grade:
        print(i)
    gradenew=addGrade(grade)
    for i in gradenew:
        print(i)
