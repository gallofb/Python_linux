class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

#1.应为是从长到短又是从根节点出发所以vaiyonng现需遍历
#2.到叶子节点满足和为给定值的路径输出：
    #从根节点开始减每次递归函数带进去的值是减去当前根节点的值如果是叶子节点且与当期函数给定的值
    #将此值返回到二维数组中
    # left和right存储路径
class Solution:
    def FindPath(self,root,expectNumber):
        if root == None:
            return[];
        temp = []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            left = self.FindPath(root.left,expectNumber-root.val)
            right = self.FindPath(root.right,expectNumber-root.val)
            for item in left+right:
                temp.append([root.val]+item)
        return item

