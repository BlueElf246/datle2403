import random
import numpy as np
def QuickSort(A,l,r):
    if l>=r:
        return
    else:
        random= np.random.randint(l,r)
        A[random],A[l]=A[l],A[random]
        m1,m2=Partition3(A,l,r)
        # A[m] is in final position
        QuickSort(A,l,m1-1)
        QuickSort(A,m2+1,r)
def Partition(A,l,r):
    x=A[l]
    j=l
    for i in range(l+1,r+1):
        if A[i] <=x:
            j=j+1
            A[j],A[i]=A[i],A[j]
    A[l],A[j]=A[j],A[l]
    return j
def Partition3(A,l,r):
    x,j,t=A[l], l, r
    for i in range(l+1, r+1):
        if A[i]<x:
            j+=1
            A[i],A[j]=A[j],A[i]
        elif A[i]>x:
            A[i],A[t]=A[t],A[i]
            t-=1
        else:
            j+=1
    A[l],A[j]=A[j],A[l]
    return j,t

lst=[2,3,2,1,2,5,6,9]
QuickSort(lst,0,len(lst)-1)
print(lst)