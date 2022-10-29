class Single_Linked_List:
    class Node:
        def __init__(self,data, next_node):
            self.data=data
            self.next=next_node
        def display(self):
            print(self.data)
            print(self.next)
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
    def delete_at_head(self):
        if self.is_empty():
            return 'the list is empty'
        else:
            self.head.data=None
            self.head=self.head.next
            self.size-=1
    def add_tail(self,e):
        new_node=self.Node(e,None)
        if self.is_empty():
            self.head=new_node
        else:
            self.tail.next=new_node
        self.tail=new_node
        self.size+=1
    def add_head(self,e):
        if self.is_empty():
            new_node = self.Node(e, None)
            self.tail=new_node
        else:
            new_node=self.Node(e,self.head)
        self.head=new_node
        self.size+=1
    def traversal(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def __iter__(self):
        current=self.head
        while current is not None:
            yield current.data
            current=current.next
arr=Single_Linked_List()

