class BST_tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add(self,data):
        data_old=data
        data=data[0]
        if self.data==data:
            return
        elif self.data[0] > data:
            if self.left:
                return self.left.add(data_old)
            else:
                self.left=BST_tree(data_old)
        elif self.data[0] < data:
            if self.right:
                return self.right.add(data_old)
            else:
                self.right=BST_tree(data_old)
    def delete(self,val):
        if self.data[0] > val:
            if self.left:
                self.left=self.left.delete(val)
        elif self.data[0] < val:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val[0])
        return self
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    def traversal_LNR(self):
        if self.left:
            self.left.traversal_LNR()
        print(self.data)
        if self.right:
            self.right.traversal_LNR()
    def search(self,id):
        if self.data[0]== id:
            return self.data
        elif self.data[0] > id:
            if self.left:
                return self.left.search(id)
        elif self.data[0]< id:
            if self.right:
                return self.right.search(id)
        return True
    def cap_nhat(self,id,ten,diachi,score):
        if self.data[0] == id:
            self.data[1]=ten
            self.data[2]=diachi
            self.data[3]=score
        elif self.data[0] > id:
            if self.left:
                return self.left.cap_nhat(id,ten,diachi,score)
        elif self.data[0]< id:
            if self.right:
                return self.right.cap_nhat(id,ten,diachi,score)
        return True
dct={1:'add student',2:'update student',3:'delete student',4:'search student'}
lst=[10,'0','0','0']
tree=BST_tree(lst)
def menu():
    count=True
    while True:
        for x in dct.keys():
            print(dct[x])
        option=int(input('chon lua chon'))
        if option==1:
            try:
                id = int(input('nhap id'))
            except:
                print('loi')
                continue
            while tree.search(id)!=True:
                print('id nay da ton tai')
                id = int(input('nhap id'))
            name=input('nhap name')
            address=input('nhap address')
            score=input('nhap score')
            lst=[id,name,address,score]
            tree.add(lst)
        if option ==2:
            try:
                id = int(input('nhap id ban muon update'))
            except:
                print('loi')
                continue
            name = input('nhap name')
            address = input('nhap address')
            score = input('nhap score')
            tree.cap_nhat(id,name,address,score)
        if option==3:
            try:
                id = int(input('nhap id ban muon delete'))
            except:
                print('loi')
                continue
            print(tree.delete(id))
        if option==4:
            try:
                id = int(input('nhap id ban muon tim kiem'))
            except:
                print('loi')
                continue
            m=tree.search(id)
            if m:
                print('id nay khong ton tai')
            else:
                print(m)


        if option==5:
            tree.traversal_LNR()

menu()

