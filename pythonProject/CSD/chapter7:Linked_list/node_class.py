class Linked_List:
    class Node:
        def __init__(self,data,next_node):
            self.data=data
            self.next=next_node
        def display(self):
            print(self.data)
            print(self.next)
    def __init__(self):
        self.head=None
        self.tail=None
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
    def remove_head(self):
        if self.is_empty():
            print('empty')
            return
        self.head=self.head.next
        if self.is_empty():
            self.tail=None
    def add_tail(self,new_data):
        new_item=self.Node(new_data,None)
        if self.is_empty():
            self.head=new_item
        else:
            self.tail.next=new_item
        self.tail=new_item
    def traversal(self):
        if self.is_empty():
            return 'empty'
        else:
            current=self.head
            while current!=None:
                print(current.data)
                current=current.next

mysll=Linked_List()

mysll.add_tail('Hello')
mysll.add_tail('CF')
mysll.add_tail('Teacher')
mysll.add_tail('Mr.Nam')
mysll.add_tail('FPTU')
print(mysll.is_empty())
mysll.traversal()
mysll.remove_head()
mysll.traversal()
