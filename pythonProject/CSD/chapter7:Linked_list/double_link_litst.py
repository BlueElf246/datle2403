class Doubly_Linked_List:
    class Node:
        def __init__(self,data,next,prev):
            self.data=data
            self.next=next
            self.prev=prev
        def display(self):
            print(self.data)
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
    def add_head(self,data):
        new=self.Node(data,None,None)
        if self.is_empty():
            self.tail=new
        else:
            new.next=self.head
            self.head.prev=new
        self.head=new
    def add_tail(self,data):
        new=self.Node(data,None,None)
        if self.is_empty():
            self.head=new
        else:
            new.prev=self.tail
            self.tail.next=new
        self.tail=new
        self.size+=1
    def remove_head(self):
        if self.is_empty():
            return 'list nay trong'
        else:
            self.head=self.head.next
            self.head.prev=None
        if self.is_empty():
            self.tail=None
        self.size-=1
    def remove_tail(self):
        if self.is_empty():
            return 'list nay trong'
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        if self.is_empty():
            self.head=None
        self.size-=1
    def __iter__(self):
        current=self.head
        while current is not  None:
            yield current.data
            current=current.next
    def traverval(self):
        if self.is_empty():
            return 'list nay trong'
        else:
            current=self.head
            while current != None:
                print(current.data)
                current=current.next
Arr=Doubly_Linked_List()
Arr.add_tail(10)
Arr.add_tail(5)
Arr.add_tail(20)
Arr.add_head(1)
Arr.add_head(2)
Arr.add_head(3)
Arr.traverval()
Arr.remove_head()
Arr.remove_head()
Arr.remove_tail()
Arr.remove_tail()

Arr.traverval()



