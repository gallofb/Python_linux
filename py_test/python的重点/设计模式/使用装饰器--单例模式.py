# # def Singleton(cls):
# #     _instance = {}
# #
# #     def _singleton(*args,**kwargs):
# #         if cls not in _instance:
# #             _instance[cls] = cls(*args,**kwargs)
# #         return _instance[cls]
# #     return _singleton
# #
# # @Singleton
# # class A():
# #     a = 1
# #     def __init__(self,x=0):
# #         self.x = x
# #
# # a1 = A(2)
# # a2 = A(3)
# # print(a1)
# # print(a2)
# #retun
#
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name,self.age)
#
# /
# v = None
# while True:
#     if v:    #将会一直用第一次调用的v
#         v.show()
#     else:
#         v = Foo('gallo','18')
#         v.show()



class Foo:
    __v = None
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

obj = Foo.get_instance()
print(obj)
#第二次执行的时候v已经有值了 因为单例模式的原因第一次已经创建的v已经存在  所以第二次直接就可以调用
obj2 = Foo.get_instance()
print(obj2)

obj3 = Foo.get_instance()
print(obj3)

#以后想用的时候直接就可以拿来用主要调用过