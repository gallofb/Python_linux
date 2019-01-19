class Node(object):
    """构建结点"""
    def __init__(self,item):
        self.elem = item
        self.l_child = None
        self.r_child = None

class Tree(object):
    """构造树"""
    def __init__(self):
    #     首结点的地址
        self.root = None
    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        # 从队列中取出当前的结点
        #左右孩子进行判断
        while queue:
            # 出队列
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)
            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)
    #广度遍历
    def breadth_travel(self):
        queue = [self.root]
        if self.root == None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)

    """先序遍历"""
    def preorder(self,node):
        if node is None:
            return
        print(node.elem,end=" ")
        self.preorder(node.l_child)
        self.preorder(node.r_child)

    """中序遍历"""
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.l_child)
        print(node.elem,end=" ")
        self.inorder(node.r_child)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.l_child)
        self.postorder(node.r_child)
        print(node.elem,end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)

