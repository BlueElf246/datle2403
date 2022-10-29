class _DoublyLinkedBase:
    class _Node:
        def __init__(self,element, prev, next):
            self.element=element
            self.next=next
            self.prev=prev
    def __init__(self):
        # create an empty list
        self._header=self._Node(None, None, None)
        self._trailer=self._Node(None, None, None)
        self._header.next=self._trailer
        self._trailer.prev=self._header
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def insert_between(self,e,prev,next):
        new=self._Node(e,prev, next)
        prev.next=new
        next.prev=new
        self._size+=1
        return new
    def delete_node(self,e):
        nex=e.next
        pre=e.prev
        pre.next=nex
        nex.prev=pre
        ans=e.element
        e.element=e.next=e.prev=None
        self._size-=1
        return ans





