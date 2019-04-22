#完全二叉树
#大根堆  任何一个树的子树最大值就是他的头
#小根堆  任何一个树的子树最小值是他的头b
#左孩子 2*i+1
#右孩子 2*i+2
class HeapSort():
    def heapSort(self,list):
        if list is None or len(list)<2:
            return

        for i in range(len(list)):
            #建立大根堆
            self.heapInsert(list,i)    #0-i

        size = len(list)-1
        list[0],list[size] = list[size],list[0]
        while size>0:
            self.heapify(list,0,size)
            size -= 1
            #再次进行最大元素与堆尾元素进行交换
            list[0],list[size] = list[size],list[0]

    def heapInsert(self,list,index):
        #如果后面的元素的值大于父节点就交换
        #可以循环到最顶端
        while list[index] > list[(index-1)//2]:
            list[index],list[(index-1)//2] = list[(index-1)//2],list[index]
            index = (index-1)//2

    #交换后让堆变成大顶堆
    def heapify(self,list,index,size):
        left = index*2+1
        while left < size:
            #先对两个子树进行比较
            if left+1 < size and list[left+1] > list[left]:
                largest = left+1
            else:
                largest = left
            largest = largest if list[largest] > list[index] else index

            if largest == index:
                break
            list[largest],list[index] = list[index],list[largest]
            index = largest
            left = index*2+1

if __name__ == '__main__':
    list = [5,6,2,1,8,2,0,3,8]
    hs = HeapSort()
    hs.heapSort(list)
    print(list)