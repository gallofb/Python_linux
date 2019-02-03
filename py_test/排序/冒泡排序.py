# 最坏时间复杂度：O(n**2)
# 最优时间复杂度：O(n)   (表示经过一次排序没有任何的元素进行交换，排序结束)
# 稳定性：稳定
def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)
    for i in range(n-1):
        flag = 0
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
        if flag == 0:
            break
    return alist

if __name__ == '__main__':
    list = [5,2,6,9,8,2]
    list = bubble_sort(list)
    print(list)