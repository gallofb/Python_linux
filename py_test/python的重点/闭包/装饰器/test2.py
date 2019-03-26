def arg_func(sex):
    def func_arg(b_func):
        def func():
            if sex == 'man':
                print("你不可以生娃")
            if sex == 'woman':
                print("你可以的")
            return b_func()
        return func
    return func_arg




@arg_func(sex='woman')
def woman():
    print("好好工作")

@arg_func
def man():
    print("好好工作")

woman()
# man()


