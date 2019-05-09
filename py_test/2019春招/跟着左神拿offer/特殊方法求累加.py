class Solution():
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self,n):
        def quisum(n):

            self.sum +=n
            n -=1
            return n>0 and self.Sum_Solution(n)
        quisum(n)
        return self.sum

if __name__ == '__main__':
    s = Solution()
    # print(s.Sum_Solution(3))
    s.Sum_Solution(3)
