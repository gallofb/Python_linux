def count(n):
    count = 0
    i = 1
    while i<=n:
        a = n // i
        b = n % i
        if a%10 == 0:
            count+=a//10*i
        elif a%10 == 1:
            count+=(a//10*i)+(b+1)
        else:
            count+=(a//10+1)*i
        i *=10

    return count

print(count(123456))
