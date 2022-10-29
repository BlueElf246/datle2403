class Doubly_linked_list:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
        def display(self):
            print(self.data)
    def __init__(self):
        self.head=self.tail=None
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
        self.head=self.head.next
        if self.is_empty():
            self.tail=None
        else:
            self.head.prev=None
    def delete_tail(self):
        if self.is_empty():
            return
        self.tail = self.tail.prev
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
    def delete_between(self,id):
        current=self.head
        if current.data==id:
            self.delete_head()
            return
        while current is not None:
            if current.data==id:
                if current.next==None:
                    self.delete_tail()
                    return
                current.prev.next=current.next
                current.next.prev=current.prev
                return
            current=current.next
    def traversal(self):
        ele=[]
        current = self.head
        while current is not None:
            ele.append(current.data)
            current=current.next
        return ele
    def minimum(self):
        min=10000000000000
        current = self.head
        while current is not None:
            if current.data<min:
                min=current.data
            current=current.next
        return min

class HashTable:
    def __init__(self,size):
        self.max=size
        self.lst=[None for i in range(self.max)]
    def get_hash(self,key):
        h = 0
        if type(key)== str:
            for char in key:
                h += ord(char)
            return h % self.max
        elif type(key)== int:
            return key % self.max
    def add(self,key,val):
        h=self.get_hash(key)
        if self.lst[h] is None:
            self.lst[h]=Doubly_linked_list()
        self.lst[h].add_tail(val)
    def get(self,key):
        h=self.get_hash(key)
        return self.lst[h].traversal()
    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.lst[h]
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.lst[h] = value
    def __delitem__(self, key):
        h=self.get_hash(key)
        self.lst[h]=None
    def check(self):
        k=[]
        for x,y in enumerate(self.lst):
            if y is None:
                k.append(x)
        print(f'cac index chua co gia tri la {k}')
    def minimum(self,index):
        m=self.lst[index]
        print(f'gia tri nho nhat trong index {index} la {m.minimum()}')
    def get_by_index(self,index):
        m=self.lst[index].traversal()
        print(f'cac gia tri trong index {index} la {m}')
h=HashTable(10)
#Nhập lần lượt các key sau vào theo thứ tự: 100,25,16,19,21,50,66,70,82,44,46,99,78,86
l=[100,25,16,19,21,50,66,70,82,44,46,99,78,86]
for x in l:
    h.add(x,x)
#Hãy xuất ra màn hình các vị trí index trong bảng băm chưa lưu trữ khóa nào
h.check()
#Hãy xuất ra danh sách các khóa được lưu trữ tại index = 6
h.get_by_index(6)
#Hãy xuất ra khóa nhỏ nhất được lưu trữ tại ']index = 0
h.minimum(0)

