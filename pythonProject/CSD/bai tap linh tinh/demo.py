import numpy as np
def a(a,b):
    return a+b,a-b,a*b,a/b
def demo1():
    x=['a','b','c','d']
    y=[c.upper() for c in x]
    print(y)
def demo2():
    x=[1,2,3,4,5,6,7,8]
    a=np.array(x)
    print(a*2)
    y=[b for b in x if b>5]
    print(y)
    z=[b*b for b in x]
    print(z)
    z=[b for b in x if b %2==0]
    print(z)
def lbd():
    result= lambda x:x**3
    print(result(10))
def lbd1(a,b):
    result=lambda x,y:x**3+y**3
    return result(a,b)
def l(x):
    return x%2==0
def lbd2(): # dung cho ham lambda dung dieu kien
    myNum=[10,5,9,2,8,6,10,8,12]
    myEven=list(filter(lambda x: (x<9),myNum))
    myEven1 = list(filter(l, myNum))
    print(myEven1,myEven)
def map1(): # dung cho ham lambda tinh toan
    myNum = [10, 5, 9, 2, 8, 6, 10, 8, 12]
    result=list(map(lambda x:x**3,myNum))
    print(result)
def spitq():
    k='dat-le-manh'
    v=k.split('-')
    for x in v:
        print(x)
    m='\n'.join([x for x in v])
    print(m)
def file():
    f=open('10000.txt', 'r+')
    string=f.read()
    list=string.split()
    print(len(list))
class rectangle():
    def __init__(self,a,b):
        self.width=a
        self.lenght=b
    def area(self):
        return self.width*self.lenght
    def perimeter(self):
        return 2*(self.width + self.lenght)
class Employee:
    def __init__(self,code,name,year,salary):
        self.code=code
        self.name=name
        self.year=year
        self.salary=salary
    def income(self):
        return self.salary*12
    def display(self):
        print(self.code,self.name,self.income())