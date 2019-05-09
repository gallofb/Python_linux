class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution():
    def __init__(self):
        self.head = None

    #头插法
    def add(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def find(self,list1,list2):
        pHead1 = self.head
    def FindFirstCommonNode(self,pHead1,pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
            if p1 is not p2:
                if p1 is None:
                    p1 = pHead2
                if p2 is None:
                    p2 = pHead1
        return p1

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.value)
            cur = cur.next


if __name__ == '__main__':
    ls1 = Solution()
    ls1.add(1)
    ls1.travel()

import imp

