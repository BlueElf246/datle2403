class ArrayQueue:
    DEFAULT_CAPACITY=3
    def __init__(self):
        self.data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self.size=0
        self.front=0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        return self.data[self.front]
    def dequeue(self):
        #remove and return the first element of the queue( FIFO)
        answer=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)% len(self.data)
        self.size-=1
        return answer
    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avail=(self. front + self. size) % len(self. data)
        self.data[avail]=e
        self.size+=1
    def resize(self,cap):
        old=self.data
        self.data=[None]*cap
        walk=self.front
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)% len(old)
        self.front=0
D=ArrayQueue()
D.enqueue(10)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(11)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(12)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(13)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(14)
print(D.data,D.front,D.size,len(D.data))
D.dequeue()
print(D.data,D.front,D.size,len(D.data))
D.enqueue(15)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(16)
print(D.data,D.front,D.size,len(D.data))
D.dequeue()
print(D.data,D.front,D.size,len(D.data))
D.enqueue(17)
print(D.data,D.front,D.size,len(D.data))
D.enqueue(18)
print(D.data,D.front,D.size,len(D.data))







