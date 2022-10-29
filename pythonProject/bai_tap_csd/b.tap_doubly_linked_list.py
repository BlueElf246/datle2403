from Positional_Linked_List import PositionalList
list=PositionalList()
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
        if x[0]==id:
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
            lst=[]
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
                lst=[id, name, age, score]
                break
            if option=='1':
                list.add_first(lst)
            elif option=='2':
                list.add_last(lst)
            print('thêm thành công')
        if option=='3':
            list.delete(list.first())
            print('xoá thành công')
        if option=='4':
            print('số lượng sinh viên là: ', list._size)
        if option=='5':
            for x in list:
                print('số id: ',x[0],' tên: ',x[1],' tuổi: ',x[2],' điểm: ',x[3])
        if option=='6':
            print('các id hiện có')
            s=[]
            for x in list:
                id=x[0]
                s.append(id)
            print(s)
            while True:
                chon=input('bạn muốn chọn id nào?')
                m=0
                for x in list:
                    if str(chon)==str(x[0]):
                        option=input('bạn chọn thay đổi name(1), age(2) hay score(3), chọn 1, 2 hoặc 3 tương ứng')
                        if option=='1':
                            name=input('nhập tên mới')
                            x[1]=name
                            m=1
                        elif option=='2':
                            age=input('nhập tuổi mới')
                            x[2]=age
                            m=1
                        elif option=='3':
                            score=input('nhập điểm mới')
                            x[3]=score
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
                id = x[0]
                s.append(id)
            print(s)
            while True:
                chon = input('bạn muốn chọn id nào')
                m=0
                for x in list:
                    if str(chon) == str(x[0]):
                        print('số id: ',x[0],' tên: ',x[1],' tuổi: ',x[2],' điểm: ',x[3])
                        m=1
                if m==1:
                    break
                else:
                    print('xin lỗi! id mà bạn cần tìm không có trong danh sách, vui lòng chọn lại')
        if option=='8':
            while True:
                chon = input('bạn muốn chọn tên nào?')
                m=0
                for x in list:
                    if str(chon) == str(x[1]):
                        print('số id: ',x[0],' tên: ',x[1],' tuổi: ',x[2],' điểm: ',x[3])
                        m=1
                if m==1:
                    break
                else:
                    print('xin lỗi! tên mà bạn cần tìm không có trong danh sách, vui lòng chọn lại')
        if option=='9':
            break

menu()