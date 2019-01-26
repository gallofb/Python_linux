class Node(object):
    """创建节点"""
    def __init__(self,value):
        self.value = value
        self.next = None

class sigle_list_reve(object):
    """使用默认参数"""
    def __init__(self,node = None):
        """保存头节点 即第一个节点"""
        self.__head = node
        if node:
            node.next = node

    """判断链表是否为空"""
    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False


    def The_length(self):
        """定义游标current进行遍历 cur指向头节点"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    """遍历链表"""
    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next!= self.__head:
            print(cur.value,end=" ")
            cur = cur.next
        print(cur.value)
    """头插法"""
    """时间复杂度O(1)"""
    def add(self,value):
        """创建节点"""
        node = Node(value)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            """最后一个节点指向头节点"""
            cur.next = self.__head

    """指定 最坏是O(n)"""
    def insert(self,value,index):
        if index <= 0:
            self.add(value)
        elif index >= self.The_length()-1:
            self.append(value)
        else:
            node = Node(value)
            count = 0
            pre = self.__head
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
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head


    """删除节点 给出值删除节点"""
    """最坏时间复杂度为O(n)"""
    def remove(self,item):
        if self.__head == None:
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.value == item:
                """当删除的是第一个节点时 pre还没有进入链表中所以直接对头节点进行操作"""
                if cur == self.__head:
                    # 头结点的删除
                    #找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #退出循环为尾结点的删除
        if cur.value == item:
            # 只有一个结点
            if cur == self.__head:
                self.__head = None
            pre.next = cur.next


    """查询数据是否存在"""
    """最坏时间复杂度为O(n)"""
    def search(self,item):
        if self.__head == None:
            return False
        cur = self.__head
        while cur.next == self.__head:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        if cur.value == item:
            return True
        return False


if __name__ == '__main__':
    li = sigle_list_reve()
    print(li.is_empty())
    li.add(1)
    li.add(2)
    print(li.The_length())
    li.travel()