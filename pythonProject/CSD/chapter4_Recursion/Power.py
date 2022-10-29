def Power(x,n):
    if n==0:
        return 1
    else:
        return x* Power(x,n-1)
print(Power(2,6))