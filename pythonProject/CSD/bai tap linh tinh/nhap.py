import ctypes


def chia(a,d):
    if a>0:
        r=a
        q=0
        while r>=d:
            r-=d
            q+=1
        return q,r
    else:
        r=a
        q=0
        while r<0:
            r+=d
            q-=1
        return q,r
l=[1,2,3,4,5,None]
def insert(data,c,value):
    for k in range(len(data)-1,c,-1):
        data[k]=data[k-1]
    data[c]=value
    print(data)

insert(l,0,10)
l=[10,1,2,3,4,5,6]
def remove(data,value):
    for i in range(0,len(data)):
        if data[i]==value:
            for m in range(i, len(data)-1):
                data[m]=data[m+1]
            data[-1]=None
            break
    print(data)
remove(l,2)