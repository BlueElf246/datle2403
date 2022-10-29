class Vector:
    def __init__(self,num):
        self.lst=[0 for x in range(0,num)]
    def add(self,b):
        c=[]
        for x in range(0,len(self.lst)):
            num=self.lst[x]+b.lst[x]
            c.append(num)
        return c
    def set_item(self,num,value):
        self.lst[num]=value
    def __setitem__(self, key, value):
        self.lst[key]=value
    def __add__(self, other):
        c = []
        for x in range(0, len(self.lst)):
            num = self.lst[x] + other[x]
            c.append(num)
        return c
    def __getitem__(self, item):
        return self.lst[item]

n=Vector(5)
n[0]=11
n[1]=2
m=Vector(5)
m[0]=9
m[1]=10
m[2]=4
total=0


class Sequence:
    def __init__(self,sq):
        self.sque=sq
        self.k=-1
    def __next__(self):
        self.k+=1
        if (self.k)<(len(self.sque)):
            return self.sque[self.k]
        else:
            raise StopIteration()
    def __iter__(self):
        return self
data=[1,2,3,4]
c=Sequence(data)
for x in c:
    print(x)
