class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def display(self):
        print(self.id, '<>', self.name, '<>', self.score)
class BST_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add(self,data):
        data_old=data
        data=data.id
        if self.data.id== data:
            return
        elif self.data.id > data:
            if self.left:
                self.left.add(data_old)
            else:
                self.left=BST_tree(data_old)
        elif self.data.id <data:
            if self.right:
                self.right.add(data_old)
            else:
                self.right=BST_tree(data_old)
    def delete(self,id,count=True):
        if self.data.id > id:
            count=False
            if self.left:
                self.left=self.left.delete(id,count)
        elif self.data.id < id:
            count=False
            if self.right:
                self.right=self.right.delete(id,count)
        else:
                if self.left is None and self.right is None:
                    if count==True:
                        print('can not delete root node')
                    return None
                elif self.left is None:
                    if count==True:
                        self.data = self.right.data
                        self.left = self.right.left
                        self.right = self.right.right
                        return
                    return self.right
                elif self.right is None:
                    if count == True:
                        self.data = self.left.data
                        self.left = self.left.left
                        self.right = self.left.right
                        return
                    return self.left
                max_val=self.left.find_max()
                self.data=max_val
                self.left=self.left.delete(max_val.id)
        return self
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    def search(self,id):
        if self.data.id == id:
            return self.data.display()
        elif self.data.id >id:
            if self.left:
                self.left.search(id)
        elif self.data.id <id:
            if self.right:
                self.right.search(id)
    def traversal(self):
        if self.left:
            self.left.traversal()
        self.data.display()
        if self.right:
            self.right.traversal()
    def capnhat(self,data1):
        if self.data.id == data1.id:
            self.data=data1
        elif self.data.id >data1.id:
            self.left.capnhat(data1)
        elif self.data.id <data1.id:
            self.right.capnhat(data1)
    def lon_nhat(self):
        element=[]
        if self.left:
            element+=self.left.lon_nhat()
        element.append((self.data.id,self.data.score))
        if self.right:
            element+=self.right.lon_nhat()
        return element
m={1:'them sv',2:'cap nhat',3:'xoa sv',4:'tim sv',5:'score lon nhat',6:'score nho nhat',7:'sap xep'}
def menu():
    count = False
    while True:
        for x in m.keys():
            print(x,'--',m[x] )
        option=int(input('nhap option'))
        if option==1:
            id=int(input('nhap id'))
            name=input('nhap name')
            score=int(input('nhap score'))
            sv=Student(id,name,score)
            if count==False:
                tree=BST_tree(sv)
                count=True
            else:
                tree.add(sv)
        if option==2:
            id = int(input('nhap id'))
            name = input('nhap name')
            score = int(input('nhap score'))
            sv = Student(id, name, score)
            tree.capnhat(sv)
        if option==3:
            id = int(input('nhap id'))
            tree.delete(id)
        if option==4:
            id = int(input('nhap id'))
            tree.search(id)
        if option==5 or option==6:
            lst = tree.lon_nhat()
            max=0
            id=0
            for x,y in lst:
                if option==5:
                    if y >max:
                        id = x
                if option==6:
                    if y < min:
                        id = x
            tree.search(id)
        if option==7:
            tree.traversal()
menu()
