class Node(object):
    """构建结点"""
    def __init__(self,item):
        self.val = item
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

    """中序遍历"""
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.l_child)
        list.append(node.val)
        # print(node.val)
        self.inorder(node.r_child)
        return list

    def isSymmetrical(self, node):
        if node is None:
            return True
        list = self.inorder_no(node)
        list2 = [str(i) for i in list]
        list3 = [str(i) for i in list]
        list3.reverse()
        print("dfdf%s" %list2)
        print(list3)
        if ''.join(list2) == ''.join(list3):
            return True
        return False
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
                sum.append(node.val)
                node = node.r_child
        return sum


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(0)
    tree.add(1)
    # tree.add(1)
    # tree.add(1)
    # tree.add(1)
    # tree.add(1)
    # print(tree.inorder_no(tree.root))
    print(tree.isSymmetrical(tree.root))


#对称二叉树

class Solution:

    def isMirror(self, r1, r2):
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False

        if r1.val == r2.val:
            return self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)
        return False

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isMirror(pRoot.left, pRoot.right)