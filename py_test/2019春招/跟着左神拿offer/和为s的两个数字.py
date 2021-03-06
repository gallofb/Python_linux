# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
         if len(array) < 2:
            return None
         return self.FindSum(array,tsum,0,len(array)-1)

    def FindSum(self,arry,sum,left,right):
        mid = sum//2
        while left<right:
            if arry[left]+arry[right] < sum:
                left +=1
            elif arry[left]+arry[right]>sum:
                right -=1
            else:
                return arry[left],arry[right]
        return None



if __name__ == '__main__':
    fs = Solution()
    list = [1,2,3,5,9,10,11,12,15,16,17,18]
    print(fs.FindNumbersWithSum(list,20))
