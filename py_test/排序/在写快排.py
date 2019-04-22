import random
class Quick_agin():
    def quick_sort(self,list):
        if len(list) < 2 or list is None:
            return
        return self.quick_sorts(list,0,len(list)-1)

    def quick_sorts(self,list,left,right):
        if(left < right):
            # q = random.randint(left,right-left+1)
            # list[q],list[right] = list[right],list[q]
            p = self.partition(list,left,right)
            # print(p)
            self.quick_sorts(list,left,p[0]-1)  #取比上次递归小的值那部分
            self.quick_sorts(list,p[1]+1,right)  #取比上一次递归大的那部分
            # print(p)

    def partition(self,list,left,right):
        less = left - 1
        more = right
        while left < more:
            if list[left] < list[right]:
                less+=1
                list[left],list[less] = list[less],list[left]
                left+=1
            elif list[left] > list[right]:
                more = more-1
                list[left],list[more] = list[more],list[left]
            else:
                left+=1
        #交换后就会形成当初less左边的小于  more右边的大于
        list[more],list[right] = list[right],list[more]
        #存储的是下标
        return [less+1,more]  #相等值的小标  #指的是和right值相同的元素  下次就不用进行计算

if __name__ == '__main__':
    list = [2,5,5,6,2,4,8,9,2,9]
    ss = Quick_agin()
    ss.quick_sort(list)
    print(list)
