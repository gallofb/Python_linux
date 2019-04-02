#单例模式  一个类的实例化返回的结果是都是同一个对象，一个类的实例从始至终只能创一次
#确保每一个类只有一个实例的存在

class User:
    _gallo = None
    _Flag = True
    def __new__(cls, *args, **kwargs):
        if cls._gallo == None:
            cls._gallo = object.__new__(cls)
        return cls._gallo

    def __init__(self,name):
        if self._Flag:
            print("init....")
            self.name = name
            self._Flag = False

u1 = User("1")
u2 = User("2")


print(u1)
print(u2)
# <__main__.User object at 0x7f3b433587f0>
# <__main__.User object at 0x7f3b433587f0>   说明a和b是同一个对象
print(u1 == u2)
