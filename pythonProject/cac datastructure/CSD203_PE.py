#Khai báo Student
class Student:
    def __init__(self,id,names,address,score):
        self.id = id
        self.names = names
        self.address = address
        self.score = score
    
    def info(self):
        print(f'Mã số: {self.id}, tên: {self.names}, địa chỉ: {self.address}, điểm: {self.score}')


# Khai báo StudentNode
class StudentNode:   
    # data ở đây chính là đối tượng Student
    def __init__(self, data, next, prev):
      self.data = data
      self.next = next
      self.prev = prev
    
    def display(self):
      self.data.info()

#Khai báo StudentDLL
class StudentDLL:
    def __init__(self):
        self.head = None
        self.tail = None 
       
    def is_empty(self):
        if self.head == None:
            return True
        return False
           
    def removeHead(self):
        if self.is_empty():
            print('Students DLL is empty')
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None   
        
        if self.is_empty():                     
            self.tail = None                    
        
    def addTail(self, newdata):
        new_item = StudentNode(newdata, None, None)
        
        if self.is_empty():
            self.head = new_item            
        else:
            self.tail.next = new_item
            self.tail.next.prev = self.tail

        self.tail = new_item    

    def addHead(self, newdata):
        new_item = StudentNode(newdata, None, None)
        if self.is_empty():        
            self.tail = new_item
        else:
            self.head.prev = new_item
            new_item.next = self.head
        
        self.head = new_item

    def removeTail(self):
        if self.is_empty():
            print('Student DLL is empty')
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
            
        self.tail = self.tail.prev
        self.tail.next = None

        if self.is_empty():                     
            self.head = None

    def traversal(self):
        if self.is_empty():
            print("Student DLL is empty")
            return
        current = self.head
        while current != None:
            current.display()
            current = current.next
    
    def isDuplicated(self,_id):
        if self.is_empty():
            return False
        current = self.head
        while current != None:
            if(current.data.id == _id):
                return True
            current = current.next
        return False
    
    def update(self,newData):
        if self.is_empty():
            print("Student DLL is empty")
            return
        current = self.head
        while current != None:
            if(current.data.id == newData.id):
                current.data.names = newData.names
                current.data.address = newData.address
                current.data.score = newData.score
                return
            current = current.next

# Chương trình chính
menu_options = {
    1: 'Thêm sinh viên (CREATE)',
    2: 'Hiển thị danh sách (READ)',
    3: 'Hiển thị thông tin sinh viên (READ)',
    4: 'Cập nhật sinh viên (UPDATE)',
    5: 'Xóa sinh viên khi biết mã số (DELETE)',
    6: 'Remove head',
    7: 'Remove tail',
    'Others': 'Thoát chương trình CRUD'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Khai báo biến lưu trữ những sinh viên
stuList = StudentDLL()

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
           maso = input("Nhập mã số: ")
           ten = input("Nhập tên: ")
           diachi = input("Nhập địa chỉ: ")
           diem = float(input("Nhập điểm: "))
           sv = Student(maso,ten,diachi,diem)
           if(stuList.isDuplicated(maso) == False):
                stuList.addTail(sv)
        elif userChoice == 2:
            stuList.traversal()
        elif userChoice == 4:
            maso = input("Nhập mã số sinh viên cần cập nhật: ")
            ten = input("Cập nhật tên: ")
            diachi = input("Cập nhật địa chỉ: ")
            diem = float(input("Cập nhật điểm: "))
            sv = Student(maso,ten,diachi,diem)
            stuList.update(sv)
        elif userChoice == 6:
            stuList.removeHead()
        elif userChoice == 7:
            stuList.removeTail()
        else:
            print('Thoát chương trình BYE BYE')
            break
