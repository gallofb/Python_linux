from functools import wraps
def reserve(func):
    @wraps(func)
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        print('来啦来啦！')
    return inner

@reserve
def breakfarst(a,b):
    print("{0}{1}饭啦".format(a,b))

@reserve
def lunch():
    print("该吃午饭啦！")



# bask = reserve(breakfarst)
# lunch = reserve(lunch)

breakfarst("A","b")
lunch()
print(lunch.__name__)