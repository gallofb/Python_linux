class Solution():
    def GetNumberOfK(self, data, k):
        if len(data) < 1:
            return 0
        leftk = self.FirstK(0,len(data)-1,data,k)
        rightk = self.Lastk(0,len(data)-1,data,k)
        if leftk != -1 and rightk != -1:
            return rightk-leftk+1
        return 0


    def Lastk(self,left,right,list,data):
        length = len(list)
        mid = (left+right) //2

        while left <= right:
            if list[mid] < data:
                left = mid + 1
            elif list[mid] > data:
                right = mid -1
            elif mid+1<length and list[mid+1]==data:
                left = mid+1
            else:
                return mid
            mid = (left + right)//2
        return -1

    def FirstK(self,left,right,list,data):
        mid = (left + right)//2
        while left <= right:
            if list[mid] < data:
                left = mid + 1
            elif list[mid] > data:
                right = mid - 1
            elif mid - 1 >= 0 and list[mid - 1] == data:
                right = mid -1
            else:
                return mid
            mid = (left + right)//2
        return -1

list = [3,3,3,3,4,5]
k = Solution()
a = k.Lastk(0,len(list),list,3)
# print(a)
print(k.GetNumberOfK(3,list))