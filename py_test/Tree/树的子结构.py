#解题思路：
    #1.首先找在树A中找和树B相同的子节点
        #如果不是继续遍历树A
    #2.判断树A中以R为根节点的字数是不是和树B具有相同的结构
        #如果是找树B中的树的结构是否与树A结构相同
    #递归的终止条件是树A或者树B的终止节点

    #Hassubtree用来检测树A的节点 判断是否符合题目要求
    #Does用来进行进行比较从A中的节点开始与B树进行比较

class Tree:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def __init__(self,node):
        self.node = None

#遍历树w
    def HasSubtree(self,root1,root2):
        #定义result初始状态为false
        reslut = False
        if root1 != None and root2!=None:
            if root1.value == root2.value:
                #如果满足就进行与B树整体比较
                reslut = self.DoesTreeeHaveTree(root1,root2)
            #不满足就进行遍历
            if not reslut:
                reslut =self.HasSubtree(root1.left,root2)
            if not reslut:
                reslut = self.HasSubtree(root1.right,root2)
        return reslut


    def DoesTreeeHaveTree(self,root1,root2):
        #如果root2为空是代表B树肯定是A的子树直接返回
        if root2 == None:
            return True
        #如果root1为空时root2肯定没有遍历完所以B树肯定不是A树的字树
        if root1 == None:
            return False
        if root1.value != root2.value:
            return False
        #同时满足一下两个条件
        return self.DoesTreeeHaveTree(root1.left,root2.left) and self.DoesTreeeHaveTree(root1.right,root2.left)

    def VerifySquenceOfBST(self, sequence):
        if len(sequence)<=0:
            return False
        left_sequnce = []
        right_sequnce =[]
        head = sequence[-1]
        for i in range(len(sequence)-1):
            if sequence[i] < head:
                left_sequnce.append(sequence[i])
            else:
                break
        while i<len(sequence)-1:
            if sequence[i] > head:
                right_sequnce.append(sequence[i])
            else:
                return False
            i +=1
        self.VerifySquenceOfBST(left_sequnce)
        self.VerifySquenceOfBST(right_sequnce)
        return True




