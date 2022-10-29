import binary_search
import dynamic_array
import fibonacci
import insertion_sort
def dynamic():
    arr=dynamic_array.DynamicArray()
    lst=[1,0,9,7,5]
    for x in lst:
        arr.append(x)
    lst1=[9,3,5,6,7,8,0,12]
    for n in lst1:
        arr.append(n)
    for y in arr:
        print(y)
def insertion():
    lst=[9,0,8,1,2,4,7,5]
    insertion_sort.insertion_sort(lst)
    print(lst)
def binary():
    data=[4,5,9,12,18,20,95,102,111,120]
    goal=int(input())
    result=binary_search.binary_search(data,goal,0,len(data)-1)
    print(result)
def fibo():
    n=int(input())
    a,b=fibonacci.good_fibonacci(n)
    print(b)
