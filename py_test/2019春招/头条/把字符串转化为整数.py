# -*- coding:utf-8 -*-
class Solution():
    def StrToInt(self, s):
        # write code here
        try:
            r = int(s)
        except:
            r = 0
        return r

if __name__ == '__main__':
    r = Solution()
    s = "a155454"
    print(r.StrToInt(s))