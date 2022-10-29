def giaithua(x):
    if x==1:
        return x
    else:
        return x*giaithua(x-1)
#big-O= n**2
def tinhtong(n):
    s=0
    for x in range(1,n+1):
        s+=giaithua(x)
    return s
print(tinhtong(7))