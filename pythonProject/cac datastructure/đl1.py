menu={1:'them sinh vien',2:'xoa sinh vien',3:'cap nhat sinh vien',4:'tim sinh vien',5:'exit'}
class doubly_linked_list:
    def __init__(self):
        self.head=self.tail=None
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=self.prev=None
        def display(self):
            self.data.info()
    class student:
        def __init__(self,id,add,age,score):
            self.id=id
            self.add=add
            self.age=age
            self.score=score
        def info(self):
            print(self.id,'--',self.add,'--',self.age,'--',self.score)
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
    def add_tail(self,data):
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
        current=self.head
        while current is not None:
            current.display()
            current=current.next
    def find_id(self,id):
        current = self.head
        while current is not None:
            if current.data.id==id:
                current.display()
                return
            current = current.next
        print('your id is not in the list')
        return
    def delete_between(self,id):
        current = self.head
        if current.data.id==id:
            self.delete_head()
            return
        while current is not None:
            if current.data.id == id:
                if current.next==None:
                    self.delete_tail()
                    return
                current.prev.next=current.next
                current.next.prev=current.prev
                return
            current = current.next
        print('your id is not in the list')
        return
    def update(self,data):
        id=data.id
        current = self.head
        while current is not None:
            if current.data.id == id:
                current.data=data
                return
            current = current.next
        print('your id is not in the list')
        return
    def check_id(self,id):
        current = self.head
        while current is not None:
            if current.data.id == id:
                return False
            current = current.next
        return True
    def nhap(self,c):
        id = input('nhap id')
        if c==1:
            while self.check_id(id) == False:
                id = input('nhap lai id')
        add = input('nhap add')
        age = input('nhap age')
        score = input('nhap score')
        data = self.student(id, add, age, score)
        return data
lst=doubly_linked_list()
def m():
    while True:
        for x in menu.keys():
            print(x,'<>',menu[x])
        try:
            option=int(input('nhap option'))
        except:
            continue
        if option==1:
            data=lst.nhap(1)
            lst.add_head(data)
        if option==2:
            id = input('nhap id')
            lst.delete_between(id)
        if option==3:
            data=lst.nhap(3)
            lst.update(data)
        if option==4:
            id = input('nhap id')
            lst.find_id(id)
        if option==5:
            print('exit...')
            break
m()






