pupils= open('data.txt', 'a+')
pupils.close()
def check(file,a):
    file.seek(0)
    for line in file:
        line=line.strip()
        if line.startswith('Roll number'):
            lst=line.split(' ')
            num=lst[-1].rstrip()
            if num== a:
                return False
    file.seek(0,2)
    return True
def show(file):
    for line in file:
        line = line.strip()
        if line.startswith('Roll'):
            lst = line.split(' ')
            print(f'avaiable roll number{lst[-1]}')
    file.seek(0)
def isdigit(b):
    if b.isalpha() == True:
        return  True
    return  False
while True:
    print('1.Report\n2.Admin\n3.Exit')
    try:
        option=int(input('vui long nhap option'))
    except:
        print('vui long nhap lai')
        continue
    if option == 2:
        print('here is the Admin menu!')
        while True:
            try:
                print('1. Create pupil record\n2. Display all pupil record\n3. Search pupil record\n4. Modify pupil record\n5. Delete pupil record\n6. Back to main menu\n')
                option1 = int(input('vui long chon option'))
            except:
                print('vui long nhap lai!')
                continue
            if option1==1:
                print('CREATE PUPIL RECORD')
                file=open('data.txt', 'a+')
                while True:
                    try:
                        while True:
                            a = input('type Roll number: ')
                            if a.isalpha()== True:
                                print('nhap lai')
                                continue
                            elif check(file, a) == True:
                                break
                            else:
                                print('hay nhap lai!')
                                continue
                        while True:
                            b = input('Enter name:')
                            if b.isalpha() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        while True:
                            c = input('Enter Mark in English:')
                            if c.isdigit() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        while True:
                            d=input('Enter Mark in Math:')
                            if d.isdigit() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        while True:
                            e=input('Enter Mark in Physics:')
                            if e.isdigit() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        while True:
                            f=input('Enter Mark in Chemistry:')
                            if f.isdigit() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        while True:
                            g=input('Enter Mark in Cs:')
                            if g.isdigit() == True:
                                break
                            else:
                                print('hay nhap lai')
                                continue
                        string = f'\nPUPIL DETAILS\nRoll number: {a}\nName: {b}\nEnglish: {c}\nMath: {d}\nPhysics: {e}\nChemistry: {f}\nCs: {g}\n'
                        file.write(string)
                        while True:
                            option2=input('Want to enter more records(y/n)?')
                            if option2=='y' or option2=='n':
                                break
                            else:
                                print('nhap lai')
                                continue
                        if option2=='y':
                            continue
                        elif option2=='n':
                            file.close()
                            break
                    except Exception as e:
                        print('vui long nhap lai')
                        print(e)
            if option1==2:
                print('DISPLAY ALL PUPIL RECORD')
                file=open('data.txt', 'r')
                for lines in file:
                    lines=lines.strip()
                    print(lines)
                file.close()
            if option1==3:
                print('SEARCH PUPIL RECORD')
                file = open('data.txt', 'r')
                show(file)
                while True:
                    try:
                        num=int(input('nhap roll number'))
                        break
                    except:
                        print('vui long thu lai')
                        continue
                count=0
                for line in file:
                    line=line.strip()
                    if count==0:
                        if line.startswith('Roll'):
                            lst=line.split(' ')
                            if int(lst[-1])==num:
                                print(line)
                                count=1
                                continue
                            else: continue
                    if count==1:
                        if line=='PUPIL DETAILS':
                            file.close()
                            break
                        print(line)
            if option1==4:
                print('MODIFY PUPIL RECORD')
                file = open('data.txt', 'r')
                lines = file.readlines()
                file.close()
                print(lines)
                while True:
                    while True:
                        num = input('type Roll number: ')
                        if num.isalpha()==True:
                            print('nhap lai')
                        else:break
                    count = None
                    for m in range(len(lines)):
                        if lines[m] == f'Roll number: {num}\n':
                            count = 1
                            continue
                        lst = lines[m].split(' ')
                        if lst[0] == '\n' and count == 1:
                            break
                        if count == 1:
                            while True:
                                decide = input(f'want to change {lines[m]}(y/n)')
                                if decide =='y' or decide=='n':
                                    break
                                else:
                                    print('nhap lai')
                                    continue
                            if decide == 'y':
                                value = input('type your value')
                                lines[m] = lst[0] + ' ' + value + '\n'
                            if decide == 'n':
                                continue
                    while True:
                        d = input('do you want to change other pupil record?(y/n')
                        if d == 'y' or d == 'n':
                            break
                        else:
                            print('nhap lai')
                            continue
                    if d == 'y':
                        continue
                    if d == 'n':
                        break
                file = open('data.txt', 'w')
                file.writelines(lines)
                file.close()
            if option1==5:
                print('DELETE PUPIL RECORD')
                file = open('data.txt', 'r')
                lines = file.readlines()
                file.close()
                print(lines)
                while True:
                    num = input('type Roll number: ')
                    count = None
                    for m in range(len(lines)):
                        if lines[m] == f'Roll number: {num}\n':
                            decide = input(f'Do you want to delete Roll number {num}(y/n)')
                            if decide == 'y':
                                lines[m] = ''
                                lines[m - 1] = ''
                            elif decide=='n':
                                break
                            count = 1
                            continue
                        lst = lines[m].split(' ')
                        if lst[0] == '\n' and count == 1:
                            break
                        if count == 1:
                            lines[m] = ''
                    while True:
                        d = input('do you want to delete other pupil record?(y/n)')
                        if d=='y' or d=='n':
                            break
                        else:
                            print('nhap lai')
                            continue
                    if d == 'y':
                        continue
                    if d == 'n':
                        break
                file = open('data.txt', 'w')
                file.writelines(lines)
                file.close()
            if option1==6:
                break
    if option==1:
        print('REPORT MENU\n')
        while True:
            print('1:CLASS RESULT\n2:PUPIL REPORT CARD\n3:BACK TO MAIN MENU')
            while True:
                try:
                    option3=int(input('vui long nhap option!'))
                    break
                except:
                    print('vui long nhap lai')
                    continue
            if option3==1:
                print('here is the Class result!')
                file = open('data.txt', 'r')
                lines = file.readlines()
                file.close()
                count = None
                string = ''
                for m in range(len(lines)):
                    lst = lines[m].split(' ')
                    if lines[m].startswith('Roll number:'):
                        new = lst[-1].strip()
                        string += new + ' '
                        count = 1
                        continue
                    if lst[0] == '\n' and count == 1:
                        continue
                    if lst[0] == 'PUPIL DETAILS\n' and count == 1:
                        continue
                    if count == 1:
                        string += lst[-1].strip() + ' '
                string = string.replace('DETAILS', '')
                l = string.split('  ')
                for x in range(len(l)):
                    l[x] = l[x].split(' ')
                print('Roll.no   Name   English    Math    Physics    Chemistry   Cs')
                for x in l:
                    s='        '.join(x)
                    s='   '+s
                    print(s)
            if option3==2:
                print('here is the pupil report card')
                file=open('data.txt', 'r')
                show(file)
                while True:
                    try:
                        num=int(input('nhap roll number'))
                        break
                    except:
                        print('vui long thu lai')
                        continue
                count=0
                for line in file:
                    line=line.strip()
                    if count==0:
                        if line.startswith('Roll'):
                            lst=line.split(' ')
                            if int(lst[-1])==num:
                                print(line)
                                count=1
                                continue
                            else: continue
                    if count==1:
                        print(line)
                        if line=='PUPIL DETAILS':
                            file.close()
                            break
            if option3==3:
                break
    if option==3:
        print('EXIT')
        exit()

























