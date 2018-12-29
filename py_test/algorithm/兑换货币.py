#假设以人民币为例，假设硬币的数量足够多。要求讲一定数额的钱兑换成硬币。要求兑换的硬币最少.
#问题用贪婪算法计算出一种结果
def change(money):
    coin = [1,2,5,10,20,50,100] #单位为分
    coin.sort(reverse=True)
    money = money*100
    result = {}

    for one in coin:
        num_coin = money//one  #除法取整
        if num_coin > 0:
            result[one] = num_coin
        remain_money = money % one     #剩余的钱
        if remain_money == 0:
            break;
        else:
            money = remain_money
    return result

if __name__ == '__main__':
    money = 6.6
    num_coin = change(money)
    result = [(key, num_coin[key]) for key in sorted(num_coin.keys())]
    for i in result:
        print(i[0],i[1])




