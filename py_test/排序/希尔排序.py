def shell_sort(alist):
    n = len(alist)
    gap = n//2  #步长

    #grp变化到0之前插入算法执行的次数
    while gap>0:
        # 插入排序
        for j in range(gap,n):
            i = j
            while i>0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
        #         如插入排序向前移动gap
                    i -= gap
                else:
                    break
        gap //=2
if __name__ == '__main__':
    list = [5,6,9,2,7,1,0,8]
    print(list)
    shell_sort(list)
    print(list)