def run():
    n=int(input())
    a=[int(i) for i in input().split()]
    product=0
    for i in range(n):
        for j in range(i+1,n):
            product=max(product,a[i]*a[j])
    print(product)
def run_fast():
    n = int(input())
    a = [int(i) for i in input().split()]
    big=0
    big2=0
    for x in a:
        if x>big:
            big=x
    for x in a:
        if x==big:
            continue
        else:
            if x >big2:
                big2=x
    print(big*big2)
def max_wise():
    a = sorted([int(i) for i in input().split()])
    print(a[-1]*a[-2])
max_wise()