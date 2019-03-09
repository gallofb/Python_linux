class Solution:
    def Permutation(self,ss):
        if ss is None:
            return;
        self.Permutation(ss,0)

    def Permutation(self,ss,start):
        if start == len(ss)-1:
            print(ss)

        for i in range(start,len(ss)):
            ss[start],ss[i] = ss[i],ss[start]
            self.Permutation(ss,start)
            ss[start],ss[i] = ss[i],ss[start]

if __name__ == '__main__':
    ss = "ab"

    a = Solution()
    a.Permutation(ss)
