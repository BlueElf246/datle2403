def input_number(x):
    while True:
        number = input(f'enter your {x} number')
        if number.isdigit():
            return number
        else:
            continue
def input_name():
    while True:
        number = input('enter your name ')
        if number.isalpha():
            return number
        else:
            print('try again')
            continue
eng=dict()
def avaiable_roll_num(eng):
    lst =''
    for i in eng:
        lst+=i+' ,'
    print(f'these are avaiable roll_number {lst}')
    num=input_number('roll')
    return num
def avaiable(num):
    for i in eng:
        if i == num:
            return True
    return False
def create_student():
    while True:
        enroll_number=avaiable_roll_num(eng)
        if avaiable(enroll_number):
            continue
        else:break
    small_dict=dict()
    name=input_name()
    english=input_number('english')
    math=input_number('math')
    small_dict['name']=name
    small_dict['math']=math
    small_dict['english']=english
    eng[enroll_number]=small_dict
def delete_student(eng):
    num=avaiable_roll_num(eng)
    for m in eng:
        if m==num:
            decide=input('do you want to delete this roll number(y/n)')
            if decide=='y':
                eng.pop(m)
                break

def modify_student(eng):
    num=avaiable_roll_num(eng)
    for m in eng:
        if m== num:
            dit=eng[m]
            for x in dit:
                decide=input(f'do you want to change:  {dit[x]} (y/n)')
                if decide=='y':
                    if x=='name':
                        change=input_name()
                    else: change=input_number(x)
                    dit[x]=change
                elif decide =='n': continue
def find_student(eng):
    num=avaiable_roll_num(eng)
    for x in eng:
        if x == num:
            print(x)
            print(eng[x])
while True:
    print('1.Report\n2.Admin\n3.Exit')
    try:
        option=int(input('vui long nhap option'))
    except:
        print('vui long nhap lai')
    if option ==2:
        while True:
            try:
                print(
                    '1. Create pupil record\n2. Display all pupil record\n3. Search pupil record\n4. Modify pupil record\n5. Delete pupil record\n6. Back to main menu\n')
                option1 = int(input('vui long chon option'))
            except:
                print('vui long nhap lai!')
                continue
            if option1 == 1:
                while True:
                    create_student()
                    decide = input('do you want more(y/n)')
                    if decide == 'y':
                        continue
                    elif decide == 'n':
                        break
            if option1 ==2 :
                for x in eng:
                    print(x, eng[x],' \n')
            if option1 ==3:
                find_student(eng)
            if option1 ==4 :
                modify_student(eng)
            if option1 ==5:
                delete_student(eng)
            if option1 ==6:
                break
    if option==1:
        print('REPORT MENU\n')
        while True:
            print('1:CLASS RESULT\n2:PUPIL REPORT CARD\n3:BACK TO MAIN MENU')
            while True:
                try:
                    option3 = int(input('vui long nhap option!'))
                    break
                except:
                    print('vui long nhap lai')
                    continue
            if option3 == 1:
                print('here is the Class result!')
                for x in eng:
                    print(x,'   ',eng[x])
            if option3==2:
                find_student(eng)
            if option3==3:
                break
    if option==3:
        exit()
