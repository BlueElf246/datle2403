def naive_solution(a,b):
    best=0
    for i in range(1,max(a,b)):
        if a%i==0 and b%i==0:
            best=i
    print(best)
def EuclidGCD(a,b):
    if b==0:
        return a
    aprime= a%b
    return EuclidGCD(b,aprime) # condition a>b, so we swap that a >b
print(EuclidGCD(101,100))