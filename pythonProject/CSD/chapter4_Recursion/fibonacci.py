def fibonacci(n1,n2,end,state=1,start=1,sum1=''):
    if start == end:
        return sum1
    if state==1:
        sum1+=str(n1)+' '+str(n2)
        state=0
        return fibonacci(n1,n2,end,state,start+1,sum1)
    elif state==0:
        sum=n1+n2
        sum1+=' '+str(sum)
        return fibonacci(n2,sum,end,state,start+1,sum1)

def khonghieu(n): #return F(n), F(n-1)
    if n==1:
        return (1,0)
    else:
        a,b=khonghieu(n-1)
        return (a+b,a)
def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def tich(n):
    lst=[]
    for x in range(2,n):
        while is_prime(x) and n%x==0:
            n=n/x
            lst.append(x)
    return lst
print(tich(7007))


