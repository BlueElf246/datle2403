import math as m
def merge_sort(lst, low, high):
    new=lst[low:(high+1)]
    print(new)
    if len(new)==1:
        return new
    else:
        mid=m.floor(low+(high-low)/2)
        B=merge_sort(lst,low,mid)
        C=merge_sort(lst,mid+1,high)
        return merge(B,C)
def merge(b,c):
    print('merge: ',b,c)
    d=[]
    len_b=len(b)
    len_c=len(c)
    i=j=0
    while i < len_b and j < len_c:
        print(b[i],'===',c[j])
        if b[i] < c[j]:
            d.append(b[i])
            i+=1
        else:
            d.append(c[j])
            j+=1
    while i < len_b:
        d.append(b[i])
        i+=1
    while j < len_c:
        d.append(c[j])
        j+=1
    print('return ',d)
    return d
lst=[2,3,9,2,9]
print(merge_sort(lst,0,len(lst)-1))
l1=[2,3,9]
l2=[2,9]

