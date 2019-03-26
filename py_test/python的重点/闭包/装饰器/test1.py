def func1(func):
    def func2():
        print(222)
        return func()
    return func2

#return func返回了一个函数对象
# return func()返回了一个函数调用

"""func1 ==> func1(myprint) ==> func2() ==> return func()==myprint()"""
@func1
def myprint():
    print("你好")

myprint()