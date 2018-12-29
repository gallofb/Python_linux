#除法
#在目前的python中除法指的就是真正的除法
a = 1/2
print(a)
# a = 0.5
# 如果要想实现以前的除法有新的操作符 // 地板除
b = 1//2
print(b)
# b = 0

c = -1/2
print(c)
# c = -0.5

d = -1//2
print(d)
# d = -1

# 仅用于整型的函数
# hex(),oct(),  将数字转化成十六进制，八进制
# chr(),ord     将ascll的数字转换为ascll 相反  适用范围 0<=num<=255