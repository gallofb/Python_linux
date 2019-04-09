class Node(object):
    """创建节点"""
    def __init__(self,x):
        self.val = x
        self.next = None

class sigle_list(object):
    """使用默认参数"""
    def __init__(self,node = None):
        """保存头节点 即第一个节点"""
        self._head = node

    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False

    def append(self,value):
        """将传入的值构造为一个节点"""
        node = Node(value)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.val,end=" ")
            cur = cur.next

    def delete(self):
        # if pHead is None:
        #     return
        # cur = pHead
        pre = None
        cur = self._head
        while cur != None:
            # pnext = cur.next
            nedel = False
            if cur.next != None and cur.next.val == cur.val:
                nedel = True
            if not nedel:
                pre = cur
                cur = cur.next
            else:
                Todel = cur
                while Todel!=None and Todel.val == cur.val:
                    Todel = Todel.next
                if pre is None:
                    self._head = Todel
                else:
                    pre.next = Todel
                cur = Todel


if __name__ == '__main__':
    li = sigle_list()
    li.append(1)
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    li.append(6)
    li.append(6)
    li.append(7)
    li.travel()
    li.delete()
    print("")
    li.travel()

