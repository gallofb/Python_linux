# -*- coding:utf-8 -*-
#栈的压如弹出序列
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV != None and popV != None and len(pushV) == len(popV):
            stack = []
            i = 0
            while popV:
                p = popV.pop(0)
                while i < len(pushV):
                    stack.append(pushV[i])

                    if pushV[i] != p:
                        # list.append(pushV[i])
                        i +=1
                    else:
                        # list.append(pushV[i])
                        i +=1
                        break
                if p == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            return True
        return False

if __name__ == '__main__':
    so = Solution()
    list1 = [1,2,3,4,5]
    list2 = [4,5,3,2,1]
    print(so.IsPopOrder(list1,list2))