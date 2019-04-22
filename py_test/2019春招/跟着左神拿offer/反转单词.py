# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        stack = s.split(" ")
        #思路
        #让没一个单词入栈,然后在出栈
        s = ' '.join(stack[::-1])
        return s

s = Solution()
print(s.ReverseSentence(""))