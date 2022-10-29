class Doublt_linked_list:
    class Node:
        def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None
        def info(self):
            self.data.display()
    class Student:
        def __init__(self,id,name,score):
            self.id=id
            self.name=name
            self.score=score
        def display(self):
            print(self.id,'<>',self.name,'<>',self.score)
    def __init__(self):
        self.head=None
        self.tail=None
    def is_empty(self):
        if self.head is None or self.tail is None:
            return True
        return False
    def add_head(self,data):
        new=self.Node(data)
        if self.is_empty():
            self.tail=new
        else:
            new.next=self.head
            self.head.prev=new
        self.head=new

    def add_tail(self, data):
        new = self.Node(data)
        if self.is_empty():
            self.head = new
        else:
            new.prev = self.tail
            self.tail.next = new
        self.tail = new
    def delete_head(self):
        if self.is_empty():
            return
        else:
            self.head=self.head.next
            if self.is_empty():
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
    def traversal(self):
        if self.is_empty():
            return
        else:
            current=self.head
            while current is not None:
                current.info()
                current=current.next
    def find_id(self,id):
        if self.is_empty():
            return
        else:
            current = self.head
            while current is not None:
                if current.data.id==id:
                    current.info()
                    return
                current = current.next
    def delete_between(self,id):
        if self.is_empty():
            return
        else:
            current = self.head
            if current.data.id==id:
                self.delete_head()
                return
            while current is not None:
                if current.data.id == id:
                    if current.next is None:
                        self.delete_tail()
                        return
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    return
                current = current.next
    def find_id_1(self,id):
        if self.is_empty():
            return
        else:
            current = self.head
            while current is not None:
                if current.data.id == id:
                    return current.data
                current = current.next
    def sap_xep(self):
        if self.is_empty():
            return
        else:
            lst=[]
            current = self.head
            while current is not None:
                lst.append(current.data.id)
                current = current.next
            lst2=[]
            lst.sort()
            for x in lst:
                lst2.append(self.find_id_1(x))
            current = self.head
            for m in lst2:
                current.data=m
                current = current.next
    def cap_nhat(self,sv):
        if self.is_empty():
            return
        else:
            current = self.head
            while current is not None:
                if current.data.id == sv.id:
                    current.data=sv
                current = current.next
    def check_id(self,id):
        if self.is_empty():
            return
        else:
            current = self.head
            while current is not None:
                if current.data.id == id:
                   return True
                current = current.next
    def lon_nhat(self):
        if self.is_empty():
            return
        else:
            max=0
            current = self.head
            while current is not None:
                if current.data.score > max:
                    max=current.data.score
                current = current.next
            current = self.head
            while current is not None:
                if current.data.score == max:
                    current.info()
                current = current.next
    def be_nhat(self):
        if self.is_empty():
            return
        else:
            min=1000000000000
            current = self.head
            while current is not None:
                if current.data.score < min:
                    min=current.data.score
                current = current.next
            current = self.head
            while current is not None:
                if current.data.score == min:
                    current.info()
                current = current.next


m={1:'add sv',2:'cap nhat sv theo id',3:'xoa sv theo id',4:'sap xep id',5:'tim sv theo id',6:'traversal',7:'be nhat',8:'lon nhat'}
lst=Doublt_linked_list()
def menu():
    while True:
        for x in m.keys():
            print(x,'--',m[x])
        try:
            option=int(input('nhap option'))
        except:
            continue
        if option==1:
            id=input('nhap id')
            while lst.check_id(id):
                id = input('nhap id')
            name=input('nhap name')
            score=int(input('nhap score'))
            sv=lst.Student(id,name,score)
            lst.add_head(sv)
        elif option==2:
            id = input('nhap id')
            name = input('nhap name')
            score = int(input('nhap score'))
            sv=lst.Student(id,name,score)
            lst.cap_nhat(sv)
        elif option==3:
            id = input('nhap id')
            lst.delete_between(id)
        elif option==4:
            lst.sap_xep()
        elif option==6:
            lst.traversal()
        elif option==7:
            lst.lon_nhat()
        elif option==8:
            lst.be_nhat()
        elif option==5:
            id = input('nhap id')
            lst.find_id(id)
menu()












