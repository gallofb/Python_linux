"""插入排序"""
#思想：
"""每次取未排序序列的最左边的元素，与一排好序的部分进行比较，如果满足条件进行互换然后前一个元素进行比较 \n
如果满足在进行互换直到与第一个元素比较完之后退出循环 默认第一个元素是已经排序好的元素"""
#改进：
"""如果第一次比较不满足条件则退出第二层循环"""
#最坏时间复杂度：O(n**2)
#最优时间复杂度：O(n)
# 稳定性：稳定
def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        #从右边的无序序列中取出多个元素执行以下过程
        # i 代表内层循环的起始值

        for j in range(i,0,-1):
        # while i>0:
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break


if __name__ == '__main__':
    li = [5,6,2,8,4,2,7,8,0,9]
    insert_sort(li)
    print(li)