"""
@gallo
eval 可以表示为python表达式的字符串 给出全局变量和局部变量,全局变量必须是字典型,局部变量可以是任何映射
eval(globals,locals) 全局,局部
"""
#有一个参数时
def test1():
    a = 10
    result = eval("a+1+a")
    print(result)

#当有全局变量时
"""这里因为有了全局变量所以,全局变量就会将a所覆盖掉所以结果如下"""
def test2():
    a=10
    g = {"a":10}
    result=eval('a+1',g)
    print(result)

#当有局部变量时
"""当局部变量和全局变量发生冲突时 局部变量 是起决定性作用的"""
def test3():
    a=10
    b=20
    c=30
    g={'a':6,'b':9}
    l={'b':100,'c':200}
    result=eval('a+b+c',g,l)
    print(result)

test1()  #21
test2()  #11
test3()  #306
