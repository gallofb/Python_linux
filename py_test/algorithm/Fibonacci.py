# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib0 = 0
        fib1 = 1
        if n == 0:
            fib= 0
        elif n == 1:
            fib= 1
        else:
            for i in range(2,n+1):
                a = fib0 + fib1
                fib0 = fib1
                fib1 = a
            fib = a
        return fib