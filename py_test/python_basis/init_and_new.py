class a(int):
    def __int__(self,value):
        super(a,self).__init__(self,abs(value))

i = a(-3)
print(i)

class b(int):
    def __new__(cls,value):
        return super(b,cls).__new__(cls,abs(value))

i = b(-3)
print(i)


