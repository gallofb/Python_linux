import random
# list = []
# for i in range(random.randint(1,100)):
#     list.append(random.randint(1,2**31-1))
# list.sort()
# print(list)
list = [random.randint(1,200) for i in range(random.randint(1,100))]
list.sort()
print(list)

