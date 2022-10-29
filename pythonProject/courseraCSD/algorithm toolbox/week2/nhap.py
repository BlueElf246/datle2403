def fibonacci_sum(n,sum=0):
    if n==1:
        return (1,0,0)
    else:
        a,b,sum=fibonacci_sum(n-1,sum)
        sum+=a
        print(a,b,sum)
        return (a+b,a,sum)
print(fibonacci_sum(10))
def div(a,d):
    q=0
    r=0
    if a>0:
        while d<=a:
            r=a-d
            q+=1
            a=r
    else:
        while a<0:
            r=a+d
            q-=1
            a=r
    print(q,r)
