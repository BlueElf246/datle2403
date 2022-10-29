class Doubly_linked_list:
    def __init__(self):
        self.head=self.tail=None
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
        def display(self):
            self.data.info()
    class student:
        def __init__(self,id,name,score):
            self.id=id
            self.name=name
            self.score=score
        def info(self):
            print(self.id,'----',self.name,'----',self.score)
    def is_empty(self):
        if self.head is None or self.tail is None
            return True
        return False
    def add_head(self,data):
        new=self.Node(data)
        if self.is_empty():
            self.tail=None
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
            return
        else:
            self.head=self.head.next
            if self.head is None:
                self.tail=None
            else:
                self.head.prev=None
    def delete_tail(self):
        if self.is_empty():
            return
        else:
            self.tail=self.tail.prev
            if self.is_empty():
                self.head=None
            else:
                self.tail.next=None
    def delete_between(self,data):
        current=self.head
        if current.data==data:
            self.delete_head()
        while current is not None:
            if current.data==data:
                if current.next is None:

                current.next.prev=current.prev
                current.prev.next=current.next

