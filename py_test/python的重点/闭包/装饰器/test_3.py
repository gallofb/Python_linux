def func1(func):
    def func2():
        print("我会写装饰器啦！！！！！")
        return func()
    return func2


@func1  #语法糖
def successful():
    print("我真的好开心啊！")

successful()




from functools import wraps
def retry(times):
    def real_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            retried_times = 0

            while True:
                try:
                    return func(*args, **kwargs)
                except Exception:

                    retried_times += 1

                    if retried_times > times:
                        raise
        return wrapper
    return real_decorator
