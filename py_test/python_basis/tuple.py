"""默认集合类型"""
"""所有函数返回的多对象都是元组类型"""
def foo1():
    # 返回的值将是一个元组
    return object,object,object

def foo2():
    #返回的是一个列表    因为返回的值是一个对象列表
    return [object,object,object]


"""单元素元组的创建"""
one_tuple = ("gallo",)
type(one_tuple)   #<class 'tuple'>