def func():
    a = 1 #外部函数作用域里面的变量
    print("你今天学习了吗？")
    def func1():  #内部函数
        print(a)
        print("今天又是元气满满的一天")
    return func1
a = func()
a()
