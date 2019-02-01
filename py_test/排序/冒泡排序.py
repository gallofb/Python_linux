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