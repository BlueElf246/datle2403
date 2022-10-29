def recursive_squaring(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return recursive_squaring(x,n/2)**2
    elif n %2!=0:
        y=recursive_squaring(x,(n-1)/2)
        return x* y*y
s=recursive_squaring(2,6)
print(s)