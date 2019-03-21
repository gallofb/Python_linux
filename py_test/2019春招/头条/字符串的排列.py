# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, list):
        # write code here
        self.all_sort(list, 0)

    def all_sort(self,list, p):
        if p == len(list):
            print(list)
        for i in range(p, len(list)):
            list[p], list[i] = list[i], list[p]
            self.all_sort(list, p + 1)
            list[p], list[i] = list[i], list[p]


if __name__ == '__main__':
    sort = Solution()
    list = ["a","b","c"]
    sort.Permutation(list)
