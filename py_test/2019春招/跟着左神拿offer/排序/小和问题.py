#coding=utf8

class Small_Sum():
    def small_sums(self,li):
        if li is None or len(li)<2:
            return 0
        return self.small_sum(li,0,len(li)-1)

    def small_sum(self,li,l,r):
        if l == r:
                return 0
        mid = l + ((r-l) // 2)
        # l = self.small_sum(li,l,mid)
        # r = self.small_sum(li,mid+1,r)
        return self.small_sum(li,l,mid) + self.small_sum(li,mid+1,r) + self.merge(li,l,mid,r)

    def merge(self,li,l,mid,r):
        res = 0
        help = []
        p1 = l
        p2 = mid+1
        while p1 <= mid and p2 <= r:
            res += (r - p2 + 1) * li[p1] if li[p1] < li[p2] else 0
            if li[p1] < li[p2]:
                help.append(li[p1])
                p1+=1
            else:
                help.append(li[p2])
                p2+=1

        while p1 <=mid:
            help.append(li[p1])
            p1 +=1

        while p2 <= r:
            help.append(li[p2])
            p2 +=1
        li[l:r+1] = help
        return res

if __name__ == '__main__':
    li = [1,2,5,4]
    ss = Small_Sum()

    sum = ss.small_sums(li)
    print(sum)

