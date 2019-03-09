# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n < 0:
            a = bin(2 ** 32 + n).replace("0b", "").count('1')
        else:
            a = bin(abs(n)).replace('0b','').count('1')
        print(a)

if __name__ == '__main__':
    s = Solution()
    s.NumberOf1(-6)