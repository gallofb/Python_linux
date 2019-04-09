class demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_information(self):
        print(self.name,self.age)

fun = demo('gallo','18')
fun.get_information()


#如果传入的参数存放在一个列表中时，用上面的方法必须对列表中的元素进行处理后才能进行上传。这样就看起来很是麻烦
#此时：classmethod就要登场了。
class demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_information(self):
        print(self.name,self.age)

    @classmethod
    def list_to_num(cls,info_list):
        return cls(info_list[0],info_list[1])


fun = demo('gallo','18')
fun.get_information()

#classmethod 的返回值传入到__init__进行初始化 ，如果init能够进行处理就自己处理，否则讲交给classmethod进行处理
list = ['zhuzhu','19']
b = demo.list_to_num(list)
b.get_information()