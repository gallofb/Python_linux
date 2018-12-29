# list = [1,2,3,4,5,6]
# list[::-1]   #[6,5,4,3,2,1]
#将一串字符串通过循环的方式每次去掉最后一个字母
# a = "abcdef"
# for i in range(-1,-len(a),-1):  #(起始位置，结束位置，间隔)
#     print(a[:i])
#     print(i)
# 如何输出abcdef
# s = enumerate(list)
# for i,q in enumerate(list,start=1):
#     print(i,q)
# enumerate 接受一个可迭代对象作为参数，返回一个enumerate对象。
# start 可以只限定序列号的初始值
#组成的是一个元组


#zip函数：用于将可迭代的对象作为参数将对象中对应的元素打包成一个元组返回对象
a = [1,2,3]
b = [3,4,5]
zippen = zip(a,b)    #返回的是一个对象
# list[zippen]
zipped = list(zippen)
print(zipped)  #转换为列表
   # exec(code, self.locals)
  # File "<input>", line 1, in <module>
# TypeError: 'list' object is not callable
# 报错的原因：之前给list复制过

# 当给zip加*时：
# 于zip相反可以理解为解压，返回二维矩阵式
a1,a2 = zip(*zip(a,b))
print(a1)
print(a2)