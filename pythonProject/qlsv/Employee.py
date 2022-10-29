class Employee:
    def __init__(self,code,name,age,salary):
        self.code=code
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print('code la:',self.code,'  ten la:',self.name,'  tuoi la:', self.age,'  luong la:',self.salary)
class Single_Linked_List:
    class Node:
        def __init__(self, data, next_node):
            self.data = data
            self.next = next_node
        def display(self):
            self.data.display()
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
    def delete_at_head(self):
        if self.is_empty():
            return 'the list is empty'
        else:
            self.head.data=None
            self.head=self.head.next
            self.size-=1
    def add_tail(self,e):
        new_node=self.Node(e,None)
        if self.is_empty():
            self.head=new_node
        else:
            self.tail.next=new_node
        self.tail=new_node
        self.size+=1
    def add_head(self,e):
        if self.is_empty():
            new_node = self.Node(e, None)
            self.tail=new_node
        else:
            new_node=self.Node(e,self.head)
        self.head=new_node
        self.size+=1
    def traversal(self):
        current=self.head
        while current is not None:
            current.display()
            current=current.next
    def find_oldest(self):
        current = self.head
        max=0
        while current is not None:
            if max < int(current.data.age):
                max=int(current.data.age)
            current = current.next
        current = self.head
        while current is not None:
            if max == int(current.data.age):
                current.display()
            current = current.next
    def __iter__(self):
        current=self.head
        while current is not None:
            yield current.data
            current=current.next
    def sum_salary(self):
        sum=0
        if self.is_empty():
            return 0
        else:
            current=self.head
            while current is not None:
                sum+=int(current.data.salary)
                current=current.next
        return sum
    def tim_theo_ma_so(self,maso):
        current = self.head
        while current is not None:
            if current.data.code==maso:
                return current.display()
            current=current.next
    def tong_nhan_vien(self):
        current = self.head
        dem=0
        while current is not None:
            dem+=1
            current = current.next
        return dem
    def luong_thap_nhat(self):
            current = self.head
            max = self.head.data.salary
            while current is not None:
                if int(max) > int(current.data.salary):
                    max = int(current.data.salary)
                current = current.next
            current = self.head
            while current is not None:
                if int(max) == int(current.data.salary):
                    current.display()
                    break
                current = current.next
    def xoa_nhan_vien(self,id):
        if self.is_empty():
            return
        elif self.tong_nhan_vien()==1:
            self.head=self.tail=None
        else:
            current=self.head
            while current is not None:
                if current.data.code == id:
                    if current.next==None:
                        current.next
                    current.next=current.next.next
                    return 'xoa thanh cong'
                current=current.next
            return 'khong tim thay id'
    def check_id(self,id):
        if self.is_empty():
            return
        else:
            current=self.head
            while current is not None:
                if current.data.code == id:
                    return True
                current=current.next
            return False
# emplist=Single_Linked_List()
# emp1=Employee(1,'dat','10','12')
# emplist.add_tail(emp1)
# emp2=Employee(2,'datle','10','12')
# emplist.add_tail(emp2)
# emplist.traversal()
list=Single_Linked_List()
def menu():
    while True:
        menu_options = {
            1: 'Thêm nhân viên',
            2: 'Hiển thị danh sách',
            3: 'Hiển thị thông tin của nhân viên theo mã số',
            4: 'Hiển thị danh sách nhân viên lớn tuổi nhất',
            5: 'Hiển thị danh sách nhân viên có lương thấp nhất',
            6: 'Trung bình lương của nhân viên',
            7: 'Tổng lương công ty phải trả hàng tháng',
            8: 'Xoá nhân viên theo mã số',
            9: 'Cập nhật thông tin nhân viên',
            'Other': 'Thoát chương trình'

        }
        while True:
            try:
                for x in menu_options.keys():
                    print(f'ấn {x} để ',menu_options[x])
                option = int(input('Chọn lựa chọn hoặc bấm số 9 (other) để thoát!'))
                break
            except:
                print('không đúng, vui lòng chọn lại!')
                continue
        if option ==1:

            id = input('nhập id')
            while list.check_id(id)== True:
                print('id nay bi trung, nhap lai id')
                id = input('nhập id')

            name = input('nhập name')
            age = input('nhập age')
            score = input('nhập score')
            emp1 = Employee(id, name, age, score)
            list.add_tail(emp1)
        elif option==2:
            list.traversal()
        elif option ==3:
            maso=input('nhap ma so')
            list.tim_theo_ma_so(maso)
        elif option ==4:
            list.find_oldest()
        elif option==5:
            list.luong_thap_nhat()
        elif option ==6:
            dem=list.tong_nhan_vien()
            sum=list.sum_salary()
            print('trung binh luong: ',float(sum/dem))
        elif option==7:
            print(list.sum_salary())
        elif option==8: # xoa nhan vien khi biet ma so
            id=input('nhap id')
            list.xoa_nhan_vien(id)
        elif option==9: #cap nhat thong tin sinh vien
            pass




menu()

