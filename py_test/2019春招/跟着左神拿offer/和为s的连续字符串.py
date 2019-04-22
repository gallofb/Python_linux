# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self,tsum):
        small = 1
        big = 2
        sum = 3
        list =[]
        # write code here
        if tsum < 3:
            return []

        while big>small:
            if sum < tsum:
                big +=1
                sum += big

            elif sum > tsum:
                sum -=small
                small +=1
            else:
                list.append(range(small,big+1))
                sum -=small
                small +=1
                # print(list)
                #
                # list = []
        return list

a = Solution()
print(a.FindContinuousSequence(100))