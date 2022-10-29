def bai1(n,x):
    # compute n*x by using addition
    if n==1:
        return x
    else:
        return x+bai1(n-1,x)

def fibonacci(n):
    # compute the nth fibonacci number
    if n==1: return 1
    elif n==2: return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def sum_odd(n):
    #compute sum of n first odd number
    if n==1:
        return 1
    else:
        return (2*n-1)+ sum_odd(n-1)
def tinh_a_mu_n(a,n):
    if n==1:
        return a
    else: return a* tinh_a_mu_n(a,n-1)
def bai5(l,x):
    l=l[:x]
    if x==0:
        return 0
    else:
        return l[-1]+bai5(l,x-1)
def tinh():
    x=5
    y=8
    s=[5,8]
    for m in range(0,100):
        sum=x+y
        s.append(sum)


