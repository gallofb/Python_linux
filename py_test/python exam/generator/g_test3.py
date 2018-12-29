def count_down(n):
    while n >= 0:
        newn = yield n
        print('newn',newn)
        if newn:
            print('if')
            n = newn
            print('n=',n)
        else:
            n -=1

cd = count_down(5)
for i in cd:
    print(i,',')
    if i == 5:
        cd.send(3)

# 自我感觉生成器应该给代码加断点然后就会有利于自己的理解...
# send的用法
#能继续使生成器往下走，但是send()传递一个值，这个值作为yield表达式的整体