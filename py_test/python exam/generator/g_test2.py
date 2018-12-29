def yeild_test(n):
    for i in range(n):
        yield i
        print("i=",i)
    print("Done")

a = yeild_test(5)
# a.__next__()
# a.__next__()
# a.__next__()
# a.__next__()
# a.__next__()
# a.__next__()

for i in yeild_test(1):
    print("--------------")

#生成器仅仅保存了一套生成数值的算法，没有让这个算法进行执行，而是在调用他的时候在执行