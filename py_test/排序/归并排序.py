#时间复杂度：
    # nlogn
    #用到的是递归的思想
    #额外空间复杂度
class Me():
    def mergesort(self,list):
        if list is None or len(list)<2:
            return
        self.mergesor(list,0,len(list)-1)  #如果长度大于2将对列表进行分组

    def mergesor(self,list,left,right):
        if left == right:         #分组中的左右下标重合时 返回
            return
        mid = left + ((right-left) // 2)  #取中间元素
        self.mergesor(list,left,mid)    #递归分组
        self.mergesor(list,mid+1,right)
        self.merge(list,left,mid,right)  #合并

    def merge(self,list,left,mid,right):
        help = []   #建立临时列表来存储某一段的排好序的元素
        p1 = left   #定义两个指针 来标记元素
        p2 = mid + 1
        while p1 <= mid and p2 <= right:  #如果同时满足时
            if list[p1] < list[p2]:
                help.append(list[p1])
                p1 +=1
            else:
                help.append(list[p2])
                p2 += 1
        while p1 <= mid:       #以下两个循环只会进去一个  向help中添加的是剩余组到指定范围的所有元素
            help.append(list[p1])
            p1 += 1
        while p2 <=right:
            help.append(list[p2])
            p2 += 1
        for i in range(len(help)):
            list[left+i] = help[i]   #help中的元素对应到被排序的list中  只改变的是list中和help元素相同的位置

if __name__ == '__main__':

    list = [2,5,1]
    me = Me()

    me.mergesort(list)
    print(list)



