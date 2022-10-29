# for x in range(10,5,-1):
#     print(x)
import math
def recursive(num):
    if num==0:
        return 1
    else:
        return num* recursive(num-1)
def a(b,exp):
    if exp==0:
        return 1
    else:
        return b * a(b,exp-1)
def gcd(a,b): #a <b
    if a==0:
        return b
    else:
        return gcd(b % a, a )
def compute_b(m,n,b):
    if n==0:
        return 1
    else:
        return (b*compute_b(m,n-1,b)) % m
def linear_search(value,list,index=0):
    n=len(list)
    if n==index:
        return 'not found'
    else:
        if list[index]== value:
            return 'found'
        else:
            return linear_search(value,list,index+1)
def string(doc): #-> run in O(n) time whereas letter+=x run in O(n**2) time
    lst=[]
    for x in doc:
        if x.isalpha():
            lst.append(x)
    letter=''.join(lst)
    return letter
n=3
for k in range(0,5):
    print(k*n)
