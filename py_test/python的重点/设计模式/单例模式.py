#单例模式  一个类的实例化返回的结果是都是同一个对象，一个类的实例从始至终只能创一次
#确保每一个类只有一个实例的存在

#使用基类
import time
class User:
    _gallo = None
    # _Flag = True
    def __new__(cls, *args, **kwargs):   #__new__是真正创建 实例的方法，以此来保证实例只有生成一个实例
        if cls._gallo is None:
            cls._gallo = object.__new__(cls)
        else:
            time.sleep(1)
        return cls._gallo

    def __init__(self,name):
        # if self._Flag:
        #     print(name)
            self.name = name
            # self._Flag = False

u1 = User("1")
u2 = User("2")


print(u1)
print(u2)

print(u1.name)
print(u2.name)

#######**************************************
    # 返回值是最后一次实例调用的原因：
        #每一次实例化都会重新调用一遍init方法  这样将上会返回的对象初始化
####### ******************************
# <__main__.User object at 0x7f3b433587f0>
# <__main__.User object at 0x7f3b433587f0>   说明a和b是同一个对象
# print(u1 == u2)
