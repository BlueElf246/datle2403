import math


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def faster_fibonacci(n):
    F=[]
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-2]+F[i-1])
    return F[n]
def binary_search(data,goal,low,high):#low is lowest index, high is highest index
    if low>high:
        return False
    else:
        print(low,high)
        mid=math.floor((low+high)/2)
        if data[mid]==goal:
            return True
        elif data[mid]<goal:
            return(binary_search(data,goal,mid+1,high))
        else:
            return(binary_search(data,goal,low,mid-1))
# data=[1,2,3,4,5,6,7]
# print(binary_search(data,9,0,len(data)-1))
