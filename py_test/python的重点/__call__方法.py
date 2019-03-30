#在定义类型的时候只要实现，__call__()方法就相当于调用实例 对象()
#或者  对象()就可以实现方法call()将会执行
class object():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("my name is {},{} years old".format(self.name,self.age))



test = object('gallo','16')
test()

