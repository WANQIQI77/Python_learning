# -----CODING: UTF-8-------
# @Author：w77
# @Time：2022/10/25 17:57
# @soft:pycharm

def applePrice(weight, price):
    allprice = weight * price
    return allprice

if __name__ == "__main__":
    a = input("苹果重量/kg:")
    b = input("苹果价格/yuan:")
    price = applePrice(int(a),int(b))
    print(price)

