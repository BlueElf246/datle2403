def fibonacci(n): #find fibonacci at nth
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
def iterative_fibonacci(n):
    if n==0:
        return 0
    else:
        x=0
        y=1
        for i in range(0,n-1):
            z=x+y
            x=y
            y=z
        return y
print(iterative_fibonacci(4))
