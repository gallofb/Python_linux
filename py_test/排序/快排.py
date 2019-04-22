# def QuickSort(list,left,right):
#     if left < right:
#         mid = Partition(list,left,right)
#
#         QuickSort(list,left,mid)
#         QuickSort(list,mid+1,right)
#     else:
#         return
#
#
# def Partition(list,left,right):
#     i = left-1
#     for j in range(left,right):
#         if list[j] <= list[right]:
#             i = i+1
#             list[i],list[j] = list[j],list[i]
#         list[i+1],list[right] = list[right],list[i+1]
#     # return i
#
# arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
# QuickSort(arr,0,len(arr)-1)


#
#
#
#
#
#
# def quick_sort(list,first,last):
#     if first >= last:
#         return
#     # n = len(list)
#     mid_value = list[first]
#     low = first
#     high = last
#     while low < high:
#         #high左移
#         while low < high and list[high] >= mid_value:
#             high -=1
#         list[low] = list[high]
#
#         while low < high and list[low] < mid_value:
#             low +=1
#         list[high] = list[low]
#     #从循环退出时low == high
#     list[low] = mid_value
#     quick_sort(list,first,low-1)
#
#     quick_sort(list,low+1,last)
#
#
# # if __name__ == '__main__':
# #     list = [1,5,9,7,2,7,2,1,3,4]
# #     print(list)
# #     quick_sort(list,0,len(list)-1)
# #     print(list)
#
#













def quick(list,first,last):
    if first >= last:
        return

    mind_value = list[first]
    low = first
    high = last
    while low < high:
        while low<high and list[high] >= mind_value:
            high -=1
        list[low] = list[high]

        while low<high and list[low] < mind_value:
            low +=1
        list[high] = list[low]

    #当high 和low 相等时：
    list[low] = mind_value
    quick(list,first,low-1)
    quick(list,low+1,last)

if __name__ == '__main__':
    list = [1,2,35,9,4,5,56,4,564,5]
    quick(list,0,len(list)-1)
    print(list)

