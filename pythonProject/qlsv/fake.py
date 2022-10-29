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
    def __iter__(self):
        current=self.head
        while current is not None:
            yield current.data
            current=current.next

# emplist=Single_Linked_List()
# emp1=Employee(1,'dat','10','12')
# emplist.add_tail(emp1)
# emp2=Employee(2,'datle','10','12')
# emplist.add_tail(emp2)
# emplist.traversal()



list=Single_Linked_List()
def check_so(x):
    if x.isdigit():
        return True
    return False
def check_chu(x):
    for m in x:
        if type(m) is str:
            pass
        else:
            return False
    return True
def check_id(id):
    for x in list:
        if x.code==id:
            print('id này đã có trong danh sách, vui lòng nhập id khác')
            return False
    return True
def menu():
    while True:
        print("""
        1.	Thêm sinh viên vào đầu danh sách
        2.	Thêm sinh viên vào cuối danh sách
        3.	Xóa sinh viên ở đầu danh sách
        4.	Đếm số lượng sinh viên
        5.	Hiện thị danh sách thông tin sinh viên, mỗi sinh viên hiển thị trên mỗi dòng theo định dạng:[id, name, age, score]
        6.	Cập nhật thông tin sinh viên
        7.	Tìm sinh viên theo mã số
        8.	Tìm sinh viên theo tên
        Other: Thoát chương trình
        """)
        while True:
            option = input('Chọn lựa chọn hoặc bấm số 9 (other) để thoát!')
            if check_so(option):
                break
            else:
                print('không đúng, vui lòng chọn lại!')
        if option=='1' or option=='2':
            while True:
                id = input('nhập id')
                if check_so(id):
                    if check_id(id):
                        pass
                    else:
                        continue
                else:
                    continue
                name = input('nhập name')
                age = input('nhập age')
                if not check_so(age):
                    continue
                score = input('nhập score')
                if not check_so(score):
                    continue
                emp1=Employee(id,name,age,score)
                break
            if option=='1':
                list.add_head(emp1)
            elif option=='2':
                list.add_tail(emp1)
            print('thêm thành công')
        if option=='3':
            list.delete_at_head()
            print('xoá thành công')
        if option=='4':
            print('số lượng sinh viên là: ', list.size)
        if option=='5':
            list.traversal()
        if option=='6':
            print('các id hiện có')
            s=[]
            for x in list:
                id=x.code
                s.append(id)
            print(s)
            while True:
                chon=input('bạn muốn chọn id nào?')
                m=0
                for x in list:
                    if str(chon)==str(x.code):
                        option=input('bạn chọn thay đổi name(1), age(2) hay score(3), chọn 1, 2 hoặc 3 tương ứng')
                        if option=='1':
                            name=input('nhập tên mới')
                            x.name=name
                            m=1
                        elif option=='2':
                            age=input('nhập tuổi mới')
                            x.age=age
                            m=1
                        elif option=='3':
                            score=input('nhập điểm mới')
                            x.salary=score
                            m=1

                if m==1:
                    print('đổi thành công')
                    break
                else:
                    print('xin lỗi! id mà bạn cần tìm không có trong danh sách, vui lòng chọn lại')
        if option=='7':
            print('các id hiện có')
            s = []
            for x in list:
                id = x.code
                s.append(id)
            print(s)
            while True:
                chon = input('bạn muốn chọn id nào')
                m=0
                for x in list:
                    if str(chon) == str(x.code):
                        print('số id: ',x.code,' tên: ',x.name,' tuổi: ',x.age,' điểm: ',x.salary)
                        m=1
                if m==1:
                    break
                else:
                    print('xin lỗi! id mà bạn cần tìm không có trong danh sách, vui lòng chọn lại')
        if option=='8':
            while True:
                n=[]
                chon = input('bạn muốn chọn tên nào?')
                for x in list:
                    name= x.name
                    n.append(name)
                print(n)
                m=0
                for x in list:
                    if str(chon) == str(x.name):
                        print('số id: ', x.code, ' tên: ', x.name, ' tuổi: ', x.age, ' điểm: ', x.salary)
                        m=1
                if m==1:
                    break
                else:
                    print('xin lỗi! tên mà bạn cần tìm không có trong danh sách, vui lòng chọn lại')
        if option=='9':
            break

menu()