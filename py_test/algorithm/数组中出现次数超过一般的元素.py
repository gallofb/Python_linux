# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers.sort()
        count = 0
        index = len(numbers)/2
        for i in range(0,len(numbers)):
            if numbers[i] == numbers[index]:
                count += 1
        if count>index:
            return numbers[index]
        else:
            return 0