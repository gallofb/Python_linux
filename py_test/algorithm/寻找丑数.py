# 题目描述
# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# 输入描述:
#
# 整数N
# 输出描述:
# 第N个丑数
# 示例1
# 输入
# 6
# 输出
# 6
"""两种思路"""
"""第一种 判断小于n的每一个数字是否是丑数"""
"""用到求丑数的方法为"""
def is_u(num):
    while num%2==0:
        num/=2
    while num%3==0:
        num/=3
    while num%5==0:
        num/=5
    if num ==1:
        return True
    return False

"""方法二"""
n = int(input())
U_num = [1]
i,j,k = 0,0,0
while max(U_num) < n:
    min_num = min(U_num[i]*2,U_num[j]*3,U_num[k]*5)
    U_num.append(min_num)
    if min_num == U_num[i]*2:
        i+=1
    if min_num == U_num[j]*3:
        j+=1
    if min_num == U_num[k]*5:
        k+=1
print(U_num)
