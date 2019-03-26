class Node(object):
    """构建结点"""
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    """构造树"""
    def __init__(self):
    #     首结点的地址
        self.root = None
    def add(self,val):
        node = Node(val)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        # 从队列中取出当前的结点
        #左右孩子进行判断
        while queue:
            # 出队列
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)
    #广度遍历
    def breadth_travel(self):
        queue = [self.root]
        if self.root == None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val,end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    """先序遍历"""
    def preorder(self,node):
        if node is None:
            return
        print(node.val,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    """中序遍历"""
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val,end=" ")
        self.inorder(node.right)

    def inorder_no(self,node):
        if node is None:
            return
        stack = []
        sum = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop(-1)
                sum.append(node.val)
                node = node.right
        return sum

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val,end=" ")


    def postorder_no(self,node):
        pass

    #镜像二叉树
    def Mirror(self,node):
        if node == None:
            return
        #只要左右子数都不为空就交换
        if node.left == None and node.right == None:
            return

        node.left,node.right = node.right,node.left
        #地柜推推倒
        self.Mirror(node.left)
        self.Mirror(node.right)

    #递归实现二叉树的遍历
    
    #从右向左
    def see_right(self,node):
        if node == None:
            return
        qunue_1 = [node]
        qunue_2 = []
        tmp_list = []
        while qunue_1 or qunue_2:
            while qunue_1:
                p = qunue_1.pop(0)
                tmp_list.append(p.val)
                if p.left:
                    qunue_2.append(p.left)
                if p.right:
                    qunue_2.append(p.right)
            print(tmp_list[-1])
            tmp_list = []

            while qunue_2:
                p = qunue_2.pop(0)
                tmp_list.append(p.val)
                if p.left:
                    qunue_1.append(p.left)
                if p.right:
                    qunue_1.append(p.right)
            print(tmp_list[-1])
            tmp_list = []

            



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
    #
    # tree.breadth_travel()
    # print(" ")
    # tree.preorder(tree.root)
    # print(" ")
    tree.inorder(tree.root)
    print(" ")
    # tree.postorder(tree.root)
    list = tree.inorder_no(tree.root)
    print(list)
    tree.see_right(tree.root)

