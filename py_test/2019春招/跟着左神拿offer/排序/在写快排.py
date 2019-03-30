class Quick_agin():
    def quick_sort(self,list):
        if len(list) < 2:
            return
        self.quick_sorts(list,0,len(list)-1)

    def quick_sorts(self,list,left,right):
        while(left < right):
            p = self.partition(list,left,right)
            self.quick_sorts(list,left,p[0]-1)
            self.quick_sorts(list,p[1]+1,right)


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
        list[more],list[right] = list[right],list[more]
        return list[less+1:more]

if __name__ == '__main__':
    list = [2,5,6,1,5,2,6]
    ss = Quick_agin()
    ss.quick_sort(list)
    print(list)
