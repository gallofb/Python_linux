#为什么要生成器
#当访问列表中大量的数据时如果只需要访问前面的几组数据绝大多数元素都是占用的空间
#白白浪费用生成器将会减少很多空间的浪费
#思考None产生的原因
def test():
    i = 0
    while i<5:
        temp =yield i
        # temp = i
        print("--------",temp,i)
        i +=1

a = test()
a.__next__()
a.__next__()
a.__next__()
a.__next__()

#出现None的原因是
#第一调用停留在了temp =yield i temp没有输出值
#第二次取值开始于print方法中所以temp没有赋值所以temp为none