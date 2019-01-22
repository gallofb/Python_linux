# 题目描述
#
# 对于三个字符串A，B，C。我们称C由A和B交错组成当且仅当C包含且仅包含A，B中所有字符，且对应的顺序不改变。请编写一个高效算法，判断C串是否由A和B交错组成。
# 给定三个字符串A,B和C，及他们的长度。请返回一个bool值，代表C是否由A和B交错组成。保证三个串的长度均小于等于100。
# 测试样例：
#
# "ABC",3,"12C",3,"A12BCC",6
#
# 返回：true
#
# 我用了比较下流的方法： 将a,b字符串组合起来然后排序，c也排序然后比较排序后的结果相等的话就返回true
class Mixture:
    def chkMixture(self, A, n, B, m, C, v):
        # write code here
        if n+m<=100 and v<=100:
            d = list(A+B)
            d.sort()
            e = list(C)
            e.sort()
            if d == e:
                return True