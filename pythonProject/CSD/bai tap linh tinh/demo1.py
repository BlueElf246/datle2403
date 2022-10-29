from demo import Employee
def input1(x):
    x=input(f'type {x}')
    return x
def check_string(x):
    return x.isalpha()
def check_digit(x):
    return x.isdigit()
def input2():
    while True:
        code=input1('code')
        year = input1('year')
        if check_digit(year):
            salary = (input1('salary'))
            if check_digit(salary):
                name=input1('name')
                if check_string(name):
                    break
        continue
#
# Employee1=Employee(code,name,year,int(salary))
# Employee1.display()
f=open('1000.data')
string=f.readlines()
counter=1
lst=[]
for line in string:
    line=line.strip()
    x=line.split(',')
    employee=Employee(x[0],x[1],int(x[2]),float(x[3]))
    lst.append(employee)

for x in lst:
    x.display()
