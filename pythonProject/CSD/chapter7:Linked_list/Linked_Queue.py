class Linked_Queue:
    class _Node:
        def __init__(self,e,next):
            self.element=e
            self.next= next
    def __init__(self):
        self._head=None
        self._tail=None
        self.size=0
    def is_empty(self):
        return self.size==0
    def __len__(self):
        return self.size
    def first(self):
        return self._head.element
    def dequeue(self):
        self._head=self._head.next
        self.size-=1
    def enqueue(self,e):
        new=self._Node(e,None)
        self._tail.next=new
        self._tail=new
        self.size+=1

