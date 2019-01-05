#用列表模拟堆栈
satck = []
# 添加一个元素到堆栈中
#入栈
def pushil(temp):
    satck.append(temp)

#出栈
def popit():
    #判断栈是否为空
    if len(satck) == 0:
        print('cannot pop from an empty stack')
    else:
        pop_temp = satck.pop()
        print("pop %s in stack",pop_temp)

