mylist = [1,2,3,4,5]
def func(obj):
    a = 1
    def func1():
        #闭包将外部函数的引用到内部函数让外部变量存活下来
        obj[0] +=a
        print('func1',obj)
    return func1

var = func(mylist)
var()
var()
var()