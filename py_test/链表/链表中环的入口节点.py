"""
解题步骤:
    1.设立两个指针 p1,p2都从头结点出发
    2,p1节点先走环的长度个节点,然后p2节点开始走,他们以相同的速度开始走,当二者相遇是就是入口节点
    3.如何求出环的长度
        1.定义一个快指针和一个慢指针快指针一次走两步慢指针一次走一步,当他们相遇是一定实在环内,
        然后记录相遇的位置然后慢指针继续走,边走边计数,当在一次返回此位置时,计数的大小就是环的长度.
"""