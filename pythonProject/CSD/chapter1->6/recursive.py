# c=[100,50,20,10,5,1]
# k=[]
# n=500
# for m in c:
#     while n>=m:
#         k.append(m)
#         n=n-m
# print(k)
# def factorial(n):
#     if n==0:
#         return 1
#     elif n>=1:
#         return n *factorial(n-1)
# print(factorial(5))
import math


def draw_line(tick_length,tick_label=''):
    line='-'*tick_length
    if tick_label:
        line+=' '+tick_label
    print(line)
def draw_interval(center_length):
    if center_length >0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)
def draw_ruler(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,num_inches+1):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))

#binary search
c=[2,3,4,5,6,7,8,9]
def binary_search(lst,number):
    length=len(lst)//2
    c1=lst[0:length]
    c2 = lst[length:]
    if length==1 and (c1[-1]==number or c2[-1]==number):
        return True
    elif c1[-1]<number:
        if length==1 and c1[-1]==number:
            return True
        elif length==1 and c1[-1]!=number:
            return False
        else:
            return binary_search(c2, number)
    elif c1[-1]>=number:
        return binary_search(c1,number)
    else:
        return False
def binary_search_1(data,target,low,high):
    if low > high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_1(data,target,low,mid-1)
        else:
            return binary_search_1(data,target,mid+1,high)
def binary_search_2(sequence, item):
    begin_index=0
    end_index=len(sequence)-1
    while begin_index <= end_index:
        mid_point=begin_index+(end_index-begin_index)//2
        mid_point_value=sequence[mid_point]
        if mid_point_value == item:
            return mid_point
        elif item < mid_point_value:
            end_index=mid_point+1
        else:
            begin_index=mid_point+1
    return None
c=[1,2,3,4,5,6,7,8]
def sum_recursive(S,n):
    if n==0:
        return 0
    else:
        return sum_recursive(S,n-1)+S[n-1]
#reversing a sequence with recursion
c1=[1,2,3,4] # -> 4,3,2,1
def reversing(c,start,stop):
    if start <stop-1:
        c[start],c[stop-1]=c[stop-1],c[start]
        reversing(c,start+1,stop-1)
def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x,n-1)
def power_1(x,n):
    if n==0:
       return 1
    else:
        partial=power_1(x,n//2)
        result=partial*partial
        if n%2 ==1:
            result =x*result
        return result
c=[1,2,3,4,5,6]
def sum_2(c,start,stop): #binary recursion
    if start >=stop: # check if c has zero element in slice
        return 0
    elif start==stop-1:
        return c[start]
    else:
        mid=(start+stop)//2
        return sum_2(c,start,mid)+sum_2(c,mid,stop)
print(sum_2(c,0,len(c)))
#multi recrusion
def puzzle_solve(k,S,U):
    for e in U:
        S+=str(e)
        U.pop(str(e))
        if k==1:
            if S=='abc':
                return S
        else:

            puzzle_solve(k-1,S,U)
c=[1,2,3,4,5,6,7,8]
def binary_search_iterative(c,target):
    low=0
    high=len(c)-1
    while low<= high:
        mid=(high+low)//2
        if c[mid]== target:
            return True
        elif target < c[mid]:
            high=mid+1
        else:
            low= mid +1
    return False
def reverse_iterative(c): # [6,5,4,3,2,1]
    l=len(c)//2
    end=len(c)-1
    for x in range(0,l):
        c[x],c[end]=c[end],c[x]
        end=end-1
    return c
print(reverse_iterative(c))


