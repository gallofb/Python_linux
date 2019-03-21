#有N个学生站成一队，顺序编号（1～N）.从第一个学生开始报数（从1到5报数），凡报道5的学生出队。队尾
#学生报完数后，队首学生在队尾学生报数基础上报数，问最后留下来的是原来的第几号那位。
def baoshu(n,ns):   #人数和要报的数字自己给定
    list = []
    for i in range(1,n+1):
        list.append(i)
    count = 0  #count来通知循环每次遍历一次count累加  直到循环结束
    while len(list)>1:
        for i in range(len(list)):
            count +=1
            if count % ns ==0:
                list.pop(i)
    return list

print(baoshu(3,5))
