class doubly_linked_list:
    def __init__(self):
        self.head=self.tail=None
    def is_empty(self):
        return self.head is None or self.tail is None
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=self.prev=None
        def info(self):
            self.data.display()
    class Student:
        def __init__(self,id,name,score):
            self.id=id
            self.name=name
            self.score=score
        def display(self):
            print(self.id,self.name,self.score)
    def add_head(self,data):
        new=self.Node(data)
        if self.is_empty():
            self.tail=new
        else:
            self.head.prev=new
            new.next=self.head
        self.head=new
    def add_tail(self,data):
        new = self.Node(data)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
            new.prev = self.tail
        self.tail = new
    def delete_head(self):
        if self.is_empty():
            print('empty!!!')
            return
        else:
            self.head=self.head.next
            if self.is_empty():
                self.tail=None
            else:
                self.head.prev=None
    def delete_tail(self):
        if self.is_empty():
            print('empty!!!')
            return
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
    def delete_between(self,data):
        current = self.head
        if current.data.id==data:
            self.delete_head()
            return
        while current is not None:
            if current.data.id==data:
                if current.next is None:
                    self.delete_tail()
                    return
                else:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    return
            current = current.next
        print('khong tim thay')
    def cap_nhat(self,data):
        current = self.head
        while current is not None:
            if current.data.id == data:
                current.data=data
                return
            current=current.next
        print('khong tim thay')
    def nhap(self):
        id=input('nhap id')
        while self.check(id):
            id = input('nhap id')
        name=input('nhap name')
        score=input('nhap score')
        data=self.Student(id,name,score)
        self.add_head(data)
    def check(self,data):
        current = self.head
        while current is not None:
            if current.data.id == data:
                return True
            current=current.next
        return False
    def find(self,data):
        current = self.head
        while current is not None:
            if current.data.id == data:
                current.info()
            current=current.next
    def find_1(self,data):
        current = self.head
        while current is not None:
            if current.data.id == data:
                return current
            current=current.next
    def sap_xep(self):
        l1=[]
        current = self.head
        while current is not None:
            l1.append(current.data.id)
            current = current.next
        l1.sort()
        l2=[]
        for x in l1:
            d=self.find_1(x)
            l2.append(d)
        for x in l2:
            x.info()
lst=doubly_linked_list()
def menu():
    m={1:'them sv',2:'xoa sv',3:'cap nhat',4:'tim sv'}
    while True:
        for x in m.keys():
            print(x, m[x])
        try:
            option=int(input('nhap option'))
        except:
            continue
        if option==1:
            lst.nhap()
        if option==2:
            id = input('nhap id')
            lst.delete_between(id)
        if option==3:
            id = input('nhap id')
            lst.cap_nhat(id)
        if option==4:
            id = input('nhap id')
            lst.find(id)
        if option==5:
            lst.sap_xep()
menu()




