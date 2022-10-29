import math
from time import time
import matplotlib.pyplot as plt
def test(filename):
    l=[]
    f=open(filename,'r+')
    f=f.readlines()
    lst=[]
    for x in f:
        x=x.strip()
        lst.append(int(x))
    goal=len(lst)
    def linear_search(lst,x):
        lst.sort()
        m=False
        for m in range(0,len(lst)):
            if lst[m] == x:
                return m
            else:
                m=False
        return m
    start=time()
    result=linear_search(lst,goal)
    end=time()
    r=(end-start)
    l.append((goal,r))
    print(result)
    # def binary_search(lst,x):
    #     lst.sort()
    #     i=0
    #     j=len(lst)
    #     while i<j:
    #         m=math.floor((i+j)/2)
    #         if x > lst[m]:
    #             i=m+1
    #         else:
    #             j=m
    #     location=i
    #     if i==len(lst):
    #         if lst[i-1]==x:
    #             return location
    #         else:
    #             return False
    #     else:
    #         return location
    # start=time()
    # location=binary_search(lst,goal)
    # end=time()
    # print(end-start)
    # r = (end - start)
    # l.append((goal, r))
    # print(location)
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
    s=time()
    print(binary_search(lst,goal))
    e=time()
    print(e-s)
    r = (e - s)
    l.append((goal, r))
    return l
# def find_max(x):
#     big=0
#     for m in x:
#         if big<m:
#             big=m
#     print(big)
# find_max(lst)
# def find_max_with_sort(x):
#     x.sort()
#     print(x[-1])
# find_max_with_sort(lst)

# l=test('10000.txt')
# print(l)
# l1=test('1000.data')
# print(l1)
# l2=test('100.txt')
# plt.plot(l,l1,l2)
# print(l2)
# plt.show()

def binary_search(arr,x):
    high=len(arr)-1
    low=0
    mid= (high+low)//2
