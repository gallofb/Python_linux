#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)<=0:
            return False
        left_sequnce = []   #存储左子树
        right_sequnce =[]   #存储右子树
        head = sequence[-1]
        i = 0
        while i <len(sequence)-1:
            if sequence[i] < head:
                left_sequnce.append(sequence[i])
                i +=1
            else:
                break
        while i<len(sequence)-1:
            if sequence[i] > head:
                right_sequnce.append(sequence[i])
            #有子树的值应该都比头结点的值大  如果不满足则不是后续遍历
            else:
                return False
            i +=1
        self.VerifySquenceOfBST(left_sequnce)
        self.VerifySquenceOfBST(right_sequnce)
        return True

if __name__ == '__main__':
    Tree = Solution()
    alist = [5,7,6,9,11,10,8]
    print(Tree.VerifySquenceOfBST(alist))

#一个死循环让我怀疑人生总以为自己的电脑坏了
