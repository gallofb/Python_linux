class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
class sigle_list(object):
    """使用默认参数"""
    def __init__(self,node = None):
        """保存头节点 即第一个节点"""
        self._head = node

    """判断链表是否为空"""
    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False


    def The_length(self):
        """定义游标current进行遍历 cur指向头节点"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历链表"""
    def travel(self):
        cur = self._head

        while cur != None:
            print(cur.value,end=" ")
            cur = cur.next

    """头插法"""
    def add(self,value):
        node = Node(value)
        node.next = self._head
        self._head = node

    def insert(self,value,index):
        if index <= 0:
            self.add(value)
        elif index >= self.The_length()-1:
            self.append(value)
        else:
            node = Node(value)
            count = 0
            pre = self._head
            while count != index-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node



    """尾插法"""
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


    """删除节点 给出值删除节点"""
    def remove(self,item):
        cur = self._head
        pre = None
        while cur!=None:
            if cur.value == item:
                """当删除的是第一个节点时 pre还没有进入链表中所以直接对头节点进行操作"""
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    """查询数据是否存在"""
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == '__main__':
    li = sigle_list()
    # print(li.is_empty())
    li.append(1)
    # li.append(2)
    # li.append(3)
    # li.insert(9,3)
    # print(li.is_empty())
    # print(li.The_length())
    print(li.search(2))
    li.travel()
    li.remove(1)
    print("")
    li.travel()
