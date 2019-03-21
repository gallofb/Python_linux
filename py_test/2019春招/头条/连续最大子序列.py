def max(array):
    if len(array) == 1:
        return array[0]
    max,sum = array[0],0
    for i in array:
        sum +=i
        if sum > max:
            max = sum
        if sum < 0:   #一直累加当sum小于零是将sum制为零
            sum = 0
    return max

array = [-1,-2,-3,-4,-5]
print(max(array))
