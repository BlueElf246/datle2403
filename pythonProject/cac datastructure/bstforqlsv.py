class Student:
    def __init__(self, id, names, address, score):
        self.id = id
        self.names = names
        self.address = address
        self.score = score

    def info(self):
        print(f'Mã số: {self.id}, tên: {self.names}, địa chỉ: {self.address}, điểm: {self.score}')


class Binary_SearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def add_child(self,data):
        data_old=data
        data=data.id
        if data == self.data.id: # if data already exist
            return
        if data < self.data.id:
            # insert in left substree
            if self.left:
                self.left.add_child(data_old)
            else:
                self.left=Binary_SearchTreeNode(data_old)
        else:
            if self.right:
                self.right.add_child(data_old)
            else:
                self.right=Binary_SearchTreeNode(data_old)
            # add in right subtree
    def in_order_traversal(self): #LNR
        element=[]
        if self.left:
            element+=self.left.in_order_traversal()
        # visit base node
        element.append(self.data.info())
        if self.right:
            element+=self.right.in_order_traversal()
        return element

    def pre_order_traversal(self): #NLR
        element=[]
        element.append(self.data.info())
        # visit left node
        if self.left:
            element+=self.left.pre_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()
        return element
    def post_order_traversal(self): #LRN
        element=[]
        if self.left:
            element+=self.left.post_order_traversal()
        if self.right:
            element+=self.right.post_order_traversal()
        element.append(self.data)
        return element

        # visit base node
    def search(self,val):
        if self.data == val:
            return True
        elif self.data > val:
            # value in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        elif self.data < val:
            # value in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right:
            return self.right.find_max()
        elif self.right is None:
            max=self.data
            return max
    def find_min(self):
        if self.left:
            return self.left.find_min()
        elif self.left is None:
            min=self.data
            return min
    def calculate_sum(self):
        sum=0
        for x in self.in_order_traversal():
            sum+=x
        return sum
    def delete_node(self,val):
        if self.data >val:
            if self.left:
                self.left=self.left.delete_node(val)
        elif self.data < val:
            if self.right:
                self.right= self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete_node(min_val)
        return self
menu_options = {
    1: 'Thêm sinh viên',
    2: 'Hiển thị danh sách',
    3: 'Hiển thị thông tin sinh viên có điểm nhỏ nhất ',
    4: 'Hiển thị thông tin sinh viên có điểm lớn nhất ',
    5: 'Xóa sinh viên khi biết mã số (DELETE)',
    'Others': 'Thoát chương trình CRUD'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Khai báo biến lưu trữ những sinh viên
count=False
while(True):
        print_menu()
        userChoice = ''
        try:
            userChoice = int(input('Nhập tùy chọn: '))
        except:
            print('Nhập sai định dạng, hãy nhập lại.....')
            continue
        #Check what choice was entered and act accordingly
        if userChoice == 1:

            maso = int(input("Nhập mã số: "))
            ten = input("Nhập tên: ")
            diachi = input("Nhập địa chỉ: ")
            diem = float(input("Nhập điểm: "))
            sv = Student(maso, ten, diachi, diem)
            if count==False:
                tree=Binary_SearchTreeNode(sv)
                count=True
            else:
                tree.add_child(sv)
        if userChoice == 2:
            tree.in_order_traversal()
        elif userChoice==3:
            print('thoát ct')
            break