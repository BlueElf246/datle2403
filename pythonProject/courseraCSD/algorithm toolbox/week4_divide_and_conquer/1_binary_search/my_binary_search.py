import math


def binary_search(lst,low,high,key):
    if high<low:
        return low-1
    mid=math.floor(low+(high-low)/2)
    if key==lst[mid]:
        return mid
    else:
        if lst[mid]>key:
            return binary_search(lst,low,mid-1,key)
        else:
            return binary_search(lst,mid+1,high,key)

lst=[2,4,4,4,7,7,9]
#print(binary_search(lst,0,len(lst)-1,4))
A=[-14,-10,2,108,108,243,285,285,285,401]
target=285
def find(A, target,low,high):
    if low>high:
        return None
    else:
        mid=math.floor(low+(high-low)/2)
        if A[mid]== target:
            if A[mid+1] > target or A[mid+1]== target:
                for x in range(mid-1,low-1,-1):
                    if A[x]==target:
                        return x
        else:
            if A[mid]>target:
                return find(A,target,low,mid-1)
            else:
                return find(A,target,mid+1,high)
print(find(A,target,0,len(A)-1))