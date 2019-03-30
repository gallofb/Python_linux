class NetherlandsFlag():
    def partition(self,list,left,right,p):
        less = left-1
        more = right+1
        while left < more:
            if list[left] < p:
                less +=1
                list[less],list[left] = list[left],list[less]   #如果小的话就自己交换
                left +=1
            elif list[left] > p:   #more值向前移动一个单位left值不用变  因为交换后要对此位置的新元素重新进行比较
                more -=1
                list[more],list[left] = list[left],list[more]
            else:   #如果相等只移动下标
                left +=1
        return
    def PrintList(self,list):
        if list is None:
            return;
        print(list)

if __name__ == '__main__':
    nlf = NetherlandsFlag()
    list = [1,2,4,4,6,7]
    nlf.PrintList(list)
    nlf.partition(list,0,len(list)-1,4)
    nlf.PrintList(list)


