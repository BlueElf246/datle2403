class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        self.tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):# return the element the FRONT of the list
        head=self.tail._next
        return head._element
    def dequeue(self):# remove and return the first element of the queue
        if self.is_empty():
            return 'empty'
        old_head=self.tail._next # which is the 1st Node
        if self._size==1:
            self.tail= None
        else:
            self.tail._next=old_head._next
        self._size-=1
        return old_head._element
    def enqueue(self,e):# Add an element to back of queue
        newest=self._Node(self,e)
        if self.is_empty():
            newest._next=newest
        else:
            newest._next=self.tail._next #which is the first node
            self.tail._next=newest
        self.tail=newest
        self._size+=1
    def rotate(self):# rotate front element to the back of the queue
        if self._size>0:
            self.tail=self.tail._next() #point to the 1st node
lst=CircularQueue()
lst.enqueue('dat')


