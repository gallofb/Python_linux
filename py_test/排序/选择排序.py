"""选择排序"""
# 思想：
"""首先在末排序序列中找到最小元素，存放在排序序列的起始位置，然后在从剩余排序元素只能怪继续寻找最小元素，然后放在已排序序列的末尾以此类推直至结束"""
# 时间复杂度  外层n  内层 n-1,n-2,n-3....近似n
#     所以时间复杂度为  O(n**2)
# 即使之前是有序的也是   O(n**2)
#
# 稳定性：不稳定
# 从小到大排序

def select_sort(alist):

    n = len(alist)
    for i in range(n-1):  #i  0～n-2
        min_index = i
        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        """只执行最后一步"""
        alist[i],alist[min_index] = alist[min_index],alist[i]

if __name__ == '__main__':
    li = [5,6,2,8,4,2,7,8,0,9]
    select_sort(li)
    print(li)