# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/23 12:07
def find_primeNumber(x):
    for i in range(2, x):
        flag = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 0
                break
        if (flag == 1):
            print(i, end=' ')


def find23(x):
    for i in range(0, x):
        if i % 2 == 0 and i % 3 == 0:
            print(i, end=' ')


if __name__ == "__main__":
    print('0-50之间的奇数')
    for i in range(1, 50, 2):
        print(i, end=' ')
    print()
    print('0-50之间的偶数')
    for i in range(2, 51, 2):
        print(i, end=' ')
    print()
    print('0-50之间的质数')
    find_primeNumber(51)
    print('同时被2和3整除的数')
    find23(51)
