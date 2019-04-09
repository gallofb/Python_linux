#python 中三种定义类方法 常规方法：self,@classmethod修饰方法，@staticmethod
# 普通方法通过self参数传递当前对象的实例，
#@class通过cls传递当前类对象.
#@static 与普通的函数一样
class A:
    def foo(self,x):
        print("foo(%s,%s)"%(self,x))
        print('self:',self)

    @classmethod
    def foo1(cls,x):
        print("foo class(%s,%s)"%(cls,x))
        print('cls:',cls)

    @staticmethod
    def foo2(x):
        print("executing static(%s)"% x)

a = A()
a.foo("1")
a.foo1("1")
a.foo2("1")

