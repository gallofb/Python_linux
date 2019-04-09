from inspect import isgeneratorfunction

def Fob(max):
    n,a,b = 0,0,1
    while n<max:
        yield b   #每一次迭代到b时停止,每一次迭代开始都是从yield的下一条开始执行
        a,b = b,a+b
        n = n+1

f = Fob(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


#每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
# 代码从 yield b 的下一条语句继续执行，# 而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。

#isgeneratorfunction()来判断此函数是否是一个生成器