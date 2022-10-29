class ArrayQueue:
    Default_capacity=10
    def __init__(self):
        self._data=[None]*ArrayQueue.Default_capacity
        self._size=0
        self._front=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            return 'list is empty'
        else:
            return self._data[self._front]
    def dequeue(self):
        element=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        print(self._data)
        print('front is',self._front)
        return element
    def enqueue(self,e):
        if self._size==len(self._data):
            self._resize(cap=2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1
        print(self._data)
        print('front is',self._front)
    def _resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)% len(old)
        self._front=0

arr=ArrayQueue()
for i in range(11):
    arr.enqueue(i)
for i in range(6):
    arr.dequeue()
for i in range(90,111):
    arr.enqueue(i)