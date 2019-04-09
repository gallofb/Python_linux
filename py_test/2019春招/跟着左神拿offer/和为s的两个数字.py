class Solution:
    def FindNumbersWithSum(self,arry,sum):
        if len(arry) < 2:
            return None
        return self.FindSum(arry,sum,0,len(arry)-1)

    def FindSum(self,arry,sum,left,right):
        mid = sum//2
        while arry[left]<=mid and arry[right] >mid:
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
    print(fs.FindNumbersWithSum(list,1))
