class doubly_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    class Node:
        def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None
    class Student:
        def __init__(self,id,name,add,score):
            self.id=id
            self.name=name
            self.add=add
            self.score=score
    def is_empty(self):
        if self.head is None or self.tail is None:
            return True
        return False
    def add_head(self,data):
        new=self.Node(data)
        if self.is_empty():
            self.tail=new
        else:
            self.head.prev=new
            new.next=self.head
        self.head=new
    def add_tail(self,data):
        new=self.Node(data)
        if self.is_empty():
            self.head=new
        else:
            self.tail.next=new
            new.prev=self.tail
        self.tail=new
    def delete_head(self):
        if self.is_empty():
            return 'None'
        else:
            self.head=self.head.next
            if self.is_empty():
                self.tail=None
            else:
                self.head.prev=None
    def delete_tail(self):
        if self.is_empty():
            return None
        else:
            self.tail=self.tail.prev
            if self.is_empty():
                self.head=None
            else:
                self.tail.next=None

    def traversal(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def deletebetween(self,id):
        current = self.head
        if current.data==id:
            self.delete_head()
            return
        while current is not None:
            if current.data==id:
                if current.next== None:
                    self.delete_tail()
                    return
                current.prev.next=current.next
                current.next.prev=current.prev
                return
            current = current.next
    def tim_id(self,id):
        current=self.head
        while current is not None:
            if current.data.id==id:
                return current.data
            current=current.next
    def sapxep(self):
        current=self.head
        lst=[]
        while current is not None:
            lst.append(current.data.id)
            current=current.next
        current=self.head
        lst1=[]
        lst.sort()
        for x in lst:
            lst1.append(self.tim_id(x))
        for m in lst1:
            current.data=m
            current=current.next
        self.traversal()
    def update(self,id,name,add,score):
        current=self.head
        while current is not None:
            if current.data.id==id:
                current.data.name=name
                current.data.add=add
                current.data.score=score
                return
            current = current.next
dll=doubly_linked_list()
dll.add_head(10)

dll.add_head(11)

dll.add_tail(12)

dll.deletebetween(10)
dll.traversal()