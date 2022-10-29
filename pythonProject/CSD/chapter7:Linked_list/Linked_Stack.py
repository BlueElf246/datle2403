class Linked_Stack:
    class _Node:
        def __init__(self,e,next):
            self.element=e
            self.next= next
    def __init__(self):
        self.head=None
        self.size=0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def push(self,e):
        self.head=self._Node(e,self.head) # create a new node, link the new node to the head and assgin old head = new node
        self.size+=1
    def top(self):
        if self.is_empty():
            return 'linked list is empty'
        else:
            return self.head.element
    def pop(self):
        ans=self.head.element
        next_of_head_node=self.head.next
        self.head=next_of_head_node
        self.size-=1
        return ans

Linked=Linked_Stack()
Linked.push(100)
Linked.push(90)
Linked.push(80)
print(Linked.top())



