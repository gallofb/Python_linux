# 按层次遍历二叉树（完全二叉树）
class Node(object):
    def __init__(self,node):
        self.node = node
        self.Lchild = None
        self.Rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,node):

        pass

    # 二叉书的层次遍历
    """用到队列先进先出的原则"""
    def travel(self):
        quene = [self.root]
        if self.root == None:
            return
        while quene:
            cur = quene.pop(0)
            print(cur.node)
            if cur.Lchild is not None:
                quene.append(cur.Lchild)
            if cur.Rchild is not None:
                quene.append(cur.Rchild)




