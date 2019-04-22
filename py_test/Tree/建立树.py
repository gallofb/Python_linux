





class Node(object):
    def __init__(self,value):
        self.value = value
        self.l_child = None
        self.r_child = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,value):
        node = Node(value)
        pass
#
# def find_postorder(preorder,inorder,postorder):
#     if len(preorder) == 0:
#         return
#     if len(preorder) == 1:
#         postorder.append(preorder[0])
#         return
#     root = preorder[0]
#     n = inorder.index(root)
#     find_postorder(preorder[1:n+1],inorder[:n],postorder)
#     find_postorder(preorder[n+1:],inorder[n+1:],postorder)
#     postorder.append(root)
#     return postorder
def find_preorder(preorder,inorder,postorder):
    if len(postorder) == 0:
        return None
    if len(postorder) == 1:
        preorder.append(postorder[0])
        return
    root = postorder[-1]
    n = inorder.index(root)
    preorder.append(root)
    find_preorder(preorder,inorder[:n],postorder[:n])
    find_preorder(preorder,inorder[n+1:],postorder[n:-1])
    return preorder

"""先序和中序找后续"""
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = Node(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1],tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])
        return root



if __name__ == '__main__':
    postorder = [7,4,2,5,8,6,3,1]
    inorder = [4,7,2,1,5,3,8,6]
    preorder = []
    print(find_preorder(preorder,inorder,postorder))
