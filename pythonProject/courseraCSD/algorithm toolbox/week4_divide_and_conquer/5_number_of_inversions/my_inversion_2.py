def naive(lst):
    count=0
    for x in range(0,len(lst)):
        for y in range(x+1,len(lst)):
            if lst[x] > lst[y] :
                count+=1
    return count
import math as m
a=[]
def merge_sort(lst, low, high):
    new=lst[low:(high+1)]
    if len(new)==1:
        return new
    else:
        mid=m.floor(low+(high-low)/2)
        B=merge_sort(lst,low,mid)
        C=merge_sort(lst,mid+1,high)
        d,count=merge_two_list(B,C)
        a.append(count)
        return d
def merge_two_list(b,c):
    i=j=0
    inversion_count=0
    d=[]
    while i < len(b) and j < len(c):
        if b[i] > c[j]:
            d.append(c[j])
            j+=1
            inversion_count+= len(b)-i
        else:
            d.append(b[i])
            i+=1
    while i < len(b):
        d.append(b[i])
        i+=1
    while j< len(c):
        d.append(c[j])
        j+=1
    return d, inversion_count
# l1=[1,6,7,20]
# l2=[3,5,8,11]
# print(merge_two_list(l1,l2))
# lst=[6,1,5,2,3]
# print(merge_sort(lst,0,len(lst)-1))
# print(sum(a))
def get_function(sequence):
    x1=0
    y1=sequence[0]
    x2=1
    y2=sequence[1]
    slope=(y2-y1)/(x2-x1)
    b=y2-(slope*x2)
    for x in range(2,5):
        y=sequence[x]
        result=int(slope)*x +int(b)
        if y==result:
            pass
        else:
            return 'Non-linear sequence'
    if b==0 and slope==1:
        result = f'f(x) = x'
    elif slope==0:
        result = f'f(x) = {int(b)}'
    elif slope ==1:
        result = f'f(x) = x + {int(b)}'
        if b<0:
            b=-b
            result = f'f(x) = x - {int(b)}'
    elif slope ==-1:
        result = f'f(x) = -x + {int(b)}'
    elif b==0:
        result = f'f(x) = {int(slope)}x'
    elif b<0:
        b=-b
        result = f'f(x) = {int(slope)}x - {int(b)}'
    else:
        result=f'f(x) = {int(slope)}x + {int(b)}'
    return result
print(get_function([1,4,7,13]))