
class Student:
    def __init__(self,data):
        self.data=data
    def check_diem(self,x):
        while True:
            decide=input(f'nhap {x}')
            if decide.isdigit():
                decide=int(decide)
                if decide >0 and decide <=10:
                    return decide
            else:
                print('nhap lai')
                continue
    def check_luachon(self,x):
        while True:
            decide=input(f'nhap {x}')
            if decide.isdigit():
                decide=int(decide)
                if decide >0 and decide <=5:
                    return decide
            else:
                print('nhap lai')
                continue
    def check_luachon_1(self,x):
        while True:
            decide=input(f'nhap {x}')
            if decide.isdigit():
                decide=int(decide)
                if decide >0 and decide <=6:
                    return decide
            else:
                print('nhap lai')
                continue
    def check_ten(self,x):
        while True:
            decide = input(f'nhap {x}')
            decide = decide.strip()
            decide = decide.upper()
            decide = decide.replace(' ', 'z')
            if decide.isalpha() == False:
                continue
            else:
                count=0
                for x in decide:
                    if x == 'z':
                        lst = decide.split('z')
                        count=1
                if count==1:
                    decide = ' '.join(lst)
                    return f' {decide} '
                else:
                    return f' {decide} '
    def check_student_id(self,x):
        while True:
            decide = input(f'nhap {x}')
            if decide.isdigit():
                decide= int(decide)
                if decide >0 and decide<99:
                    return decide
            else:
                print('nhap lai')
                continue
    def avaiable_roll_num(self,eng):
        lst =''
        for i in eng:
            lst+=str(i)+' ,'
        print(f'these are available roll_number {lst}')
        print('choose your id want to change')
        num=self.check_student_id('id')
        return num
    def avaiable_roll_num_1(self,eng):
        lst =''
        for i in eng:
            lst+=str(i)+' ,'
        print(f'these are avaiable roll_number {lst}')
        print('choose your id want to change')
    def modify_student(self,eng):#seq.txt
        num=self.avaiable_roll_num(eng)
        decide=input('Do you want to change this student_id(y/n)')
        if decide =='y':
            for i in eng:
                if i == num:
                    while True:
                        new_student_id = self.check_student_id(' new id')
                        if student.if_exist(new_student_id)== True:
                            break
                        else:continue
                    dict_of_the_key=(eng[num])
                    eng.pop(num)
                    eng[new_student_id]=dict_of_the_key
                    num=new_student_id
                    break
        for m in eng:
            if m== num:
                dit=eng[m]
                for x in dit:
                    decide=input(f'do you want to change:  {x}: {dit[x]}  in id {m}(y/n)')
                    if decide=='y':
                        if x=='Name':
                            change=self.check_ten('ten')
                        else: change=self.check_diem(x)
                        dit[x]=change
                    elif decide =='n': continue
    def if_exist(self,x):
        for m in self.data:
            if m ==x:
                print('this id was signed, please choose other id!')
                return False
        return True

    def insertion_sort(self,list_a):
        indexing_length = range(1, len(list_a))
        for i in indexing_length:
            value_to_sort = list_a[i]

            while list_a[i - 1] > value_to_sort and i > 0:
                list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
                i = i - 1
        return list_a
def change(x):
    string = str(list(x.values()))
    string = string.replace("['", '  ')
    string = string.replace("',", '')
    string = string.replace(', ', '         ')
    string = string.replace(']', '')
    string=string.replace('  ','     ')
    return string
def show():
    print('ID          NAME         MATH                 PHYSICS           CHEMISTRY           AVERAGE GRADE(IF REQUIRED)')
data=dict()
student=Student(data)
while True:
    print('Chon lua chon\n1/Input Data\n2/Remove Data\n3/Edit Data\n4/Display Data\n5/Exit')
    decide=student.check_luachon('lua chon')
    if decide == 1:
        print('INPUT DATA')
        while True:
            Student_id = student.check_student_id('Student_id')
            if student.if_exist(Student_id) == True:
                break
            else:continue
        Name=student.check_ten('Name')
        Math_point=student.check_diem('Math point')
        Physics_Point=student.check_diem('Physic_Point')
        Chemistry_Point=student.check_diem('Chemistry_Point')
        sub_data_1=dict()
        sub_data_1['Name']=Name
        sub_data_1['Math point']=Math_point
        sub_data_1['Physics_Point']=Physics_Point
        sub_data_1['Chemistry_Point']=Chemistry_Point
        student.data[Student_id]=sub_data_1
    if decide==2:
        print('REMOVE DATA')
        student.avaiable_roll_num_1(student.data)
        decide=input('Do you want to delete by name or by student_id (1 for name or 2 for stu_id)?')
        if decide==str(2):
            Student_id = student.check_student_id('Student_id')
        if decide==str(1):
            name = student.check_ten('Ten')
        count=0
        for x in student.data:
            if decide==str(2):
                if x ==Student_id:
                    print('Dang thuc hien xoa bang student_id')
                    student.data.pop(x)
                    print('Da xong')
                    count=1
                    break
            elif decide ==str(1):
                dict_int_key=student.data[x]
                for m in dict_int_key:
                    if m=='Name':
                        print('Dang thuc hien xoa bang name')
                        student.data.pop(x)
                        print('Da xong')
                        count=1
                        break
            if count==0:
                print('name or id is not valid!')
                break
            break
    if decide==3:
        print('EDIT DATA')
        student.modify_student(student.data)
    if decide==4:
        print('DISPLAY DATA')
        print('\n1/BY NAME A-Z\n2/BY NAME Z-A\n3/BY MATH POINT\n4/BY PHYSICS POINT\n5/BY CHEMISTRY POINT\n6/BY AVERAGE POINT')
        decide = student.check_luachon_1('CHON OPTION')
        lst = list(student.data.items())
        if decide == 1:
            name_list = list()
            print('BY NAME A_Z')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                name = dict_in_key['Name']
                name_list.append(name)
            name_list=sorted(name_list)
            count=0
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Name']
                    name_m=f'{x}'
                    if name == name_m:
                        if count <len(name_list):
                            count+=1
                            string=change(tuple[1])
                            print(tuple[0], string)
        if decide == 2:
            name_list = list()
            print('BY NAME Z_A')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                name = dict_in_key['Name']
                name_list.append(name)
            name_list=sorted(name_list)
            name_list=name_list[::-1]
            count=0
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Name']
                    name_m=f'{x}'
                    if name == name_m:
                        if count <len(name_list):
                            count+=1
                            string = change(tuple[1])
                            print(tuple[0],string)
        if decide == 3:
            name_list = list()
            print('BY NAME MATH_POINT')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                name = dict_in_key['Math point']
                name_list.append(name)
            name_list=student.insertion_sort(name_list)
            name_list = name_list[::-1]
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Math point']
                    if name == x:
                        string = change(tuple[1])
                        print(tuple[0], string)
        if decide == 4:
            name_list = list()
            print('BY NAME PHYSICS POINT')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                name = dict_in_key['Physics_Point']
                name_list.append(name)
            name_list=student.insertion_sort(name_list)
            name_list = name_list[::-1]
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Physics_Point']
                    if name == x:
                        string = change(tuple[1])
                        print(tuple[0], string)
        if decide == 5:
            name_list = list()
            print('BY NAME CHEMISTRY POINT')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                name = dict_in_key['Chemistry_Point']
                name_list.append(name)
            name_list=student.insertion_sort(name_list)
            name_list = name_list[::-1]
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Chemistry_Point']
                    if name == x:
                        string = change(tuple[1])
                        print(tuple[0], string)
            continue
        if decide == 6:
            name_list = list()
            print('BY AVERAGE POINT')
            show()
            for tuple in lst:
                dict_in_key = tuple[1]
                Chemistry = dict_in_key['Chemistry_Point']
                Math = dict_in_key['Math point']
                Physics = dict_in_key['Physics_Point']
                Average_point = (Chemistry + Math + Physics) / 3
                dict_in_key['Average point'] = Average_point
                name_list.append(Average_point)
            name_list = student.insertion_sort(name_list)
            name_list = name_list[::-1]
            for x in name_list:
                for tuple in lst:
                    dict_in_key = tuple[1]
                    name = dict_in_key['Average point']
                    if name == x:
                        string = change(tuple[1])
                        print(tuple[0], string)
    if decide==5:
        print('EXIT')
        print('bye bye')
        exit()
    print('\n\n')











