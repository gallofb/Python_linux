def QuickSort(list,left,right):
    if left < right:
        mid = Partition(list,left,right)

        QuickSort(list,left,mid)
        QuickSort(list,mid+1,right)
    else:
        return


def Partition(list,left,right):
    i = left-1
    for j in range(left,right):
        if list[j] <= list[right]:
            i = i+1
            list[i],list[j] = list[j],list[i]
        list[i+1],list[right] = list[right],list[i+1]
    return i

arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
QuickSort(arr,0,len(arr)-1)