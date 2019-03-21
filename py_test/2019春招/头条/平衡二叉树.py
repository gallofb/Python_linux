#平衡二叉树的概念：
    #是一颗空树或者左右两个树的高度差的绝对值不超过1
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
    #     首结点的地址
        self.root = None
    def add(self,item):
        node = TreeNode(item)
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
                
    def IsBalanced_Solution(self,pRoot):
        if pRoot is None:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self,pRoot):
        if pRoot == None:
            return 0
        nleft = self.TreeDepth(pRoot.left)
        nright = self.TreeDepth(pRoot.right)
        return max(nleft+1,nright+1)

    def preorder(self,node):
        if node is None:
            return
        print(node.val,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)


if __name__ == '__main__':
    Tree = Solution()
    Tree.add(1)
    Tree.add(2)
    Tree.add(3)
    Tree.add(4)
    Tree.add(5)
    Tree.add(6)
    Tree.add(7)
    # Tree.preorder(Tree.root)
    Tree.IsBalanced_Solution(Tree.root)
    print(Tree.IsBalanced_Solution(Tree.root))