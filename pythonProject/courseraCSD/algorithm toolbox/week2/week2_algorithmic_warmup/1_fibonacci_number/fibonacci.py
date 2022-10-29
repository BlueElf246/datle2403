# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
def fibonacci(n):
    F=list()
    F.append(0)
    F.append(1)
    for x in range(2,n+1):
        F.append(F[x-1]+F[x-2])
    return F[-1]
n = int(input())
print(fibonacci(n))
