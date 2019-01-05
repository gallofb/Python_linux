def reserve(number):
    a =1
    b = 1
    if number<=0:
        return 0
    else:
        for i in range(1,number+1):
            a,b = b,a+b
        return a

def rectCover(number):
        # write code here
    if number <= 2:
        return number
    first = 1
    second = 2
    for i in range(2, number):
        first, second = second, first+second
    return second

result = reserve(0)
re = rectCover(0)
print(result,re)