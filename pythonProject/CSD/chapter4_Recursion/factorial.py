import math


def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
def factorial_1(x):
    p=1
    for m in range(1,x+1):
        p*=m
    return p


