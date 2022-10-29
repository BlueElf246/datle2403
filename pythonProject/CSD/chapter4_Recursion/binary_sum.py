import math
def binary_sum(x):
    if len(x)==1:
        return x[0]
    mid=math.floor(len(x)/2)
    print(x[:mid],x[mid:])
    l1=x[:mid]
    l2=x[mid:]
    return binary_sum(l1)+binary_sum(l2)
def linear_sum(x):
    sum=0
    for m in x:
        sum+=m
    return sum
def recursive_sum(x,n):
    if n==0:
        return x[0]
    else:
        return x[n]+recursive_sum(x,n-1)
lst=[10,10,10,10,10]
m=recursive_sum(lst,len(lst)-1)
def recursive_sum(x,n):
    if n==0:
        return 0
    else:
        return x[n-1]+recursive_sum(x,n-1)
def inverted_list(x,m,string=''):
    if m==0:
        return string
    string+=str(x[m-1])
    return inverted_list(x,m-1,string)
lst=[0,1,2,3]
def inverted(x,m):
    if m==0:
        return
    inverted(x,m-1)
    print(x[m-1])
inverted(lst,len(lst))
def basic_ruler(data,n):
    if n==0:
        return
    print('--')
    print(data[n-1])
    print('--')
    print('--')
    print('-')
    print('-')
    print('-')
    basic_ruler(data,n-1)
basic_ruler(lst,len(lst))