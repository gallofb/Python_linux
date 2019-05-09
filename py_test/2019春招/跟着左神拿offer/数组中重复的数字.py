"""此方法来自于剑指offer 时间复杂度为O(n),空间复杂度为O(1)"""


# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers):
        if numbers is None or len(numbers)<=0:
            return False

        for i in range(len(numbers)):
            if numbers[i]<0 or numbers[i]>len(numbers)-1:
                return False

        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    return True
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
        return False



s = Solution()
numbers = [2,3,1,0,2,5,3]
print(s.duplicate(numbers))