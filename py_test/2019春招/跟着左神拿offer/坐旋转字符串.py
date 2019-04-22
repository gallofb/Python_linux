# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) <1:
            return ""
        if n%len(s) == 0:
            return s
        else:
            k = n%len(s)
            new_s = s[k:len(s)]+s[0:k]
            return new_s

st = Solution()
c = st.LeftRotateString("",3)
print(c)