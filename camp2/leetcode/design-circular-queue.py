"""
we can implment using array and  linked list


"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.front=-1
        self.end = -1
        self.size = k

        

    def enQueue(self, value: int) -> bool:
        # check weather queue is full or not 
        if (self.end+1)%self.size == self.front:
            return 
        elif self.end==-1:
            self.front = 0
            self.end = 0
            self.queue[self.end] = value
        else:
            self.end = (self.end+1)%self.size
            self.queue[self.end] = value
        return True
        


        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front==self.end:
            removed_element = self.queue[self.front]
            self.front =-1
            self.end = -1
        else:
            removed_element = self.queue[self.front]
            self.front = (self.front+1)%self.size
            
        return True

        

    def Front(self) -> int:
        if self.end==self.front==-1:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.end==self.front==-1:
            return -1
        return self.queue[self.end]
        

    def isEmpty(self) -> bool:
        return self.front==self.end==-1
        

    def isFull(self) -> bool:
        return  (self.end+1)%self.size == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()