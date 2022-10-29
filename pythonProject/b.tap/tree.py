class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def display(self):
        print(self.id, self.name, self.score)
class BST_tree:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
    def add(self,data):
        data_old=data
        data=data.id
        if self.data.id==data:
            return
        elif self.data.id > data:
            if self.left:
                self.left.add(data_old)
            else:
                new=BST_tree(data_old)
                self.left=new
        elif self.data.id < data:
            if self.right:
                self.right.add(data_old)
            else:
                new = BST_tree(data_old)
                self.right=new
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data
    def delete(self,data):
        data_old=data
        data=data.id
        if self.data.id >data:
            if self.left:
                self.left=self.left.delete(data_old)
        elif self.data.id < data:
            if self.right:
                self.right=self.right.delete(data_old)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min=self.right.min()
            self.data=min
            self.right=self.right.delete(min.id)
        return self
    def traversal(self):
        if self.left:
            self.left.traversal()
        self.data.display()
        if self.right:
            self.right.traversal()
s=Student(1,2,3)
s1=Student(2,2,3)
tree=BST_tree(s)
tree.add(s1)
tree.traversal()

