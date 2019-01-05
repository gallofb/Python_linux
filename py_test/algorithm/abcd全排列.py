def nexP(list,start):
    if start==len(list)-1:
        print(list)
    for i in range(start,len(list)):
        list[start],list[i] = list[i],list[start]
        nexP(list,start+1)
        #加这一步的原因：
        #由于是start和i进行交换所以start的值是不能变的所以每次交换完之后应该在把他归为上一步
        list[start],list[i] = list[i],list[start]
if __name__ == '__main__':
    list = ['a','b','c']
    nexP(list,0)
