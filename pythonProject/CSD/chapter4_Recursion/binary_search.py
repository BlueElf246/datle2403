import math
from time import time
f=open('data.txt','r+')
f=f.readlines()
lst=[]
for x in f:
    x=x.strip()
    lst.append(int(x))
def binary_search(lst,target):
    lst.sort()
    if len(lst)==1 and lst[0]==target:
     return True
    elif len(lst)==1 and lst[0]!=target:
     return False
    else:
     mid=math.ceil(len(lst)/2)
     l1=lst[:mid]
     l2=lst[mid:]
     if l1[-1] < target:
         return binary_search(l2,target)
     else:
         return binary_search(l1,target)
def binary(data,goal,low,high):
    print(data[low:high+1])
    print(low,high)
    if low>high:
        return False
    else:
        mid=math.floor((low+high)/2)
        if data[mid]==goal:
            return True
        elif data[mid]<goal:
            return binary(data,goal,mid+1,high)
        else:
            return binary(data,goal,low,mid-1)

a=[4,5,9,12,18,20,95,102,111,120]
print(binary(a,111,0,len(a)-1))
