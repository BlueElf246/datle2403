class Student:

    __data = []
    listStudents = []



    def addStudent(self):
        infor = {
            'id': '',
            'name': '',
            'Điểm toán': '',
            'Điểm lý': '',
            'Điểm hóa': ''
        }

        # Nhập ID, có kiểm tra trùng ID thì nhập lại
        print("Nhập ID sinh viên:")
        id = int(input())

        while True:

            if id > 99:
                print("ID này không hợp lệ, vui lòng nhập lại:")
                id = int(input())
            else:
                break

        infor['id'] = id

        # Nhập tên
        print("Nhập tên sinh viên:")
        infor['name'] = input().title()



        print('nhập điểm toán:')
        diemtoan = float(input())
        while True:
            if diemtoan > 10:
                print('điểm không hợp lệ, nhập lại')
                diemtoan = float(input())
            else:
                break
        infor['Điểm toán'] = diemtoan

        print('nhập điểm lý:')
        diemly = float(input())
        while True:
            if diemly > 10:
                print('điểm không hợp lệ, nhập lại')
                diemly = float(input())
            else:
                break
        infor['Điểm lý'] = diemly

        print('nhập điểm hóa:')
        diemhoa = float(input())
        while True:
            if diemhoa > 10:
                print('điểm không hợp lệ, nhập lại')
                diemhoa = float(input())
            else:
                break
        infor['Điểm hóa'] = diemhoa

        self.listStudents.append(infor)
        print(self.listStudents)



    def findID(self , id):
        for i in self.listStudents:
            if i['id'] == id:
                return i
        return False
    def findID_1(self , id):
        for i in self.listStudents:
            if i['id'] == id:
                return True

        return False
    def deleteStudents(self):
        print("Nhập ID sinh viên cần xóa:")
        id = int(input())

        student = self.findID_1(id)

        if student != False:
            for i in range(len(self.listStudents)):
                if self.listStudents[i]['id']== id:
                    self.listStudents.pop(i)
                    print("Xóa sinh viên thành công")
        else:
            print("Không tìm thấy sinh viên cần xóa")



    def showStudents(self):

        print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
        for i in self.listStudents:
            print(i)


    def editStudent(self):
        print("Nhập ID sinh viên cần sửa")
        id = input()
        student = self.findID(id)
        if student == False:
            print("Không tìm thấy sinh viên ", id)
        else:
            print("Nhập tên sinh viên")
            name = input().title()
            student[1]['name'] = name
            self.listStudents[student[0]] = student[1]
            print('Nhập điểm toán:')
            diemtoan = float(input())
            while True:
                if diemtoan > 10:
                    print('điểm không hợp lệ, nhập lại')
                    diemtoan = float(input())
                else:
                    break
            student[1]['Điểm toán'] = diemtoan
            diemly = float(input())
            while True:
                if diemly > 10:
                    print('điểm không hợp lệ, nhập lại')
                    diemly = float(input())
                else:
                    break
            student[1]['Điểm lý'] = diemly
            diemhoa = float(input())
            while True:
                if diemhoa > 10:
                    print('điểm không hợp lệ, nhập lại')
                    diemhoa = float(input())
                else:
                    break
            student[1]['Điểm hóa'] = diemhoa
            self.listStudents[student[0]] = student[1]







