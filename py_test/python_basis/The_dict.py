"""fromkeys来适合创建一个默认的字典"""
fdict = {}.fromkeys(('a','b'))

"""工厂方法 dict()来创建字典  通过二元组列表来创建"""
fdict2 = dict((['a','b'],[1,2]))

"""通过dict()和关键字来创建"""
fdict3 = dict(a=1,b=2,c=3)

"""也可以直接给字典变量和值"""
fdict4 = {'a':1,'b':2,'c':3}


# 如何访问字典
"""通过迭代器来访问字典"""
# for key in fdict4:
    # print("key=%s,value=%s" %(key,fdict4[key]))

"""或者通过keys()方法"""

"""适用于字典的输出方法"""
print("for dict key={},other key={}".format("a","b"))