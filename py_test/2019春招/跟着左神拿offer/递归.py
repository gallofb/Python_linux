#找一个数组中的最大值

def fin_nax(list,left,right):
    if left == right:
        return list[left]

    mid = (left+right)//2
    max_left = fin_nax(list,left,mid)
    max_right = fin_nax(list,mid+1,right)
    return max(max_left,max_right)

list = [1,1,4,8,6,0,2,4]
max = fin_nax(list,0,len(list)-1)
print(max)


#所谓递归函数就是系统栈  逻辑（自己调用自己啊）
# 函数调子过程之前会把自己的   **所有信息**   都保存在栈中
#当调用结束返回时再将系统栈中的内容取出来
# 时间复杂度满足 ：2T(N/2) = nlogn

