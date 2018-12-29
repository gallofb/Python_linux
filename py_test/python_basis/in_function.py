class Foo:
    pass
foo = Foo()
class Bar(object):
    pass
bar = Bar()

# type(Foo)
print(type(Foo))
print(type(foo))
print(type(Bar))
print(type(bar))

#tpye 检测变量属于那一变量类型
#ininstance 检测变量是否属于某一变量类型 返回bool(isinstance(object,classinfo))
#object 是变量     #classinfo是一种变量类型或者是元组的形式


#type 和 isinstance 的相同之处
# 1.都是用来检测变量的是否属于某一变量类型

#不同之处
#isinstance 能判断出class类的  子类  实例化对象是否属于父类而type是不可以的
#
class A():
    pass
class B(A):
    pass

print(isinstance(B(),A))
print(type(A())==A)   #不是子类可以