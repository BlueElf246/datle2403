def prefix_average(x):
    n=len(x)
    A=[0]*n
    for j in range(n):
        total=0
        for i in range(j+1):
            total+=x[i]
    return total
def tong(x):
    t=0
    for m in x:
        t+=m
    return t
def ting(x):
    for i in range(x):
        t=0
        for j in range(1,i+2):
            t+=j
    return t


s=[1,2,3,4,5]
print(prefix_average(s))
print(tong(s))
print(ting(3))