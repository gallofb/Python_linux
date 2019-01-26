class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Double_link(object):
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        if self.__head == None:
            return True
        return False

    def length(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.__head
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        print(cur.value)
        while cur!= None:
            print(cur.value,end=" ")
            cur = cur.next



    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next!=None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,index,item):
        if index <=0:
            self.add(item)
        elif index > self.length()-1:
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while count<index:
                count +=1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def search(self,item):
        cur = self.__head
        while cur!=None:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.value == item:
                if cur == self.__head:
                    self.__head = cur.next
                    """如果长度大于一"""
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prex = cur.prev
                break
            cur = cur.next

if __name__ == '__main__':
    li = Double_link()
    li.append(1)
    li.add(2)
    li.append(3)
    li.add(4)
    li.insert(0,9)
    li.insert(8,5)
    li.remove(9)
    print(li.length())
    li.travel()
