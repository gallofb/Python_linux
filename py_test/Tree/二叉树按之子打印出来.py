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
    def inorder_no(self,node):
        if node is None:
            return
        stack = []
        sum = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.l_child
            else:
                node = stack.pop(-1)
                sum.append(node.elem)
                node = node.r_child
        return sum
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.l_child)
        self.postorder(node.r_child)
        print(node.elem,end=" ")
    def postorder_no(self,node):
        pass
    #镜像二叉树
    def Mirror(self,node):
        if node == None:
            return
        #只要左右子数都不为空就交换
        if node.l_child == None and node.r_child == None:
            return

        node.l_child,node.r_child = node.r_child,node.l_child
        #地柜推推倒
        self.Mirror(node.l_child)
        self.Mirror(node.r_child)
    def zhi_print(self,node):
        result = []
        if node is None:
            return result
        stack1 = [node]
        stack2 = []
        while stack1 or stack2:
            # r = []
            while stack1:
                cur_node = stack1.pop()
                result.append(cur_node.elem)
                if cur_node.l_child:
                    stack2.append(cur_node.l_child)
                if cur_node.r_child:
                    stack2.append(cur_node.r_child)
            # if r:
            #     result.append(r)
            # r = []
            while stack2:
                cur_node = stack2.pop()
                result.append(cur_node.elem)
                if cur_node.r_child:
                    stack1.append(cur_node.r_child)
                if cur_node.l_child:
                    stack1.append(cur_node.l_child)
            # if r:
            #     result.append(r)
        return result

    def Print(self, node):
        # write code here
        if node==None:
            return []
        odd=[]
        even=[]
        res=[]
        odd.append(node)
        while odd or even:
            r=[]
            while odd:
                temp=odd.pop()
                r.append(temp.elem)
                if temp.l_child:
                    even.append(temp.l_child)
                if temp.r_child:
                    even.append(temp.r_child)
            if r:
                res.append(r)
            r=[]
            while even:
                temp=even.pop()
                r.append(temp.elem)
                if temp.r_child:
                    odd.append(temp.r_child)
                if temp.l_child:
                    odd.append(temp.l_child)
            if r:
                res.append(r)
        return res


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
    # list = tree.inorder_no(tree.root)
    # print(list)
    print(tree.zhi_print(tree.root))
    print(tree.Print(tree.root))

