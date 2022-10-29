# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def fibonacci(n):
    F=list()
    F.append(0)
    F.append(1)
    for x in range(2,n+1):
        F.append(F[x-1]+F[x-2])
    return F[-1]
def run(n,m):
    x=fibonacci(n)
    result= x% m
    return result
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(run(n, m))
