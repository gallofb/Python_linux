#使用type创建类

# 创建A类
class A:
    bar = True


print(A)
#********||************
A1 = type('A1',(),{'bar':True})
print(A1)

#继承A类

class child_A(A):
    def echo_bar(self):
        print(self.bar)

child_A1 = type('child_A1',(A1,),{})


print(child_A)
print(child_A1)



def echo_bar(self):
    print(self.bar)

child_A2 = type('child_A2',(A1,),{'echo_bar':echo_bar})
hasattr(child_A2,'echo_bar')
my_a = child_A2()
my_a.echo_bar()