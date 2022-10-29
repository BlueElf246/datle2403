class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def info(self):
        print(self.id,'--',self.name,'--',self.score)
class BST_tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add(self,data):
        data_old=data
        data=data.id
        if self.data.id==data:
            return
        elif self.data.id > data:
            if self.left:
                return self.left.add(data_old)
            else:
                self.left=BST_tree(data_old)
        elif self.data.id < data:
            if self.right:
                return self.right.add(data_old)
            else:
                self.right=BST_tree(data_old)
    def delete_node(self,val):
        if self.data.id > val:
            if self.left:
                self.left=self.left.delete_node(val)
        elif self.data.id < val:
            if self.right:
                self.right=self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete_node(max_val.id)
        return self
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_max()
    def traversal(self):
        if self.left:
            self.left.traversal()
        self.data.info()
        if self.right:
            self.right.traversal()

m={1:'them sv',2:'hien thi danh sach', 3:'hien thi nho nhat',4:'hien thi lon nhat',5:'xoa theo id'}
def menu():
    count = False
    while True:
        for x in m.keys():
            print(x,'--',m[x])
        option=int(input('chon option'))
        if option==1:
            id=int(input('nhap id'))
            name=input('nhap name')
            score=input('nhap score')
            sv=Student(id,name,score)
            if count==False:
                tree=BST_tree(sv)
                count=True
            else:
                tree.add(sv)
        if option==2:
            tree.traversal()
        if option==3:
            tree.find_min()
        if option==4:
            tree.find_max()
        if option==5:
            id=int(input('nhap id'))
            tree.delete_node(id)

menu()
