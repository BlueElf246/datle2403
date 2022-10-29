# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10
def fibonacci_sum(n,sum=0):
    if n==1:
        return (1,0,0)
    else:
        a,b,sum=fibonacci_sum(n-1,sum)
        sum+=a
        return (a+b,a,sum)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(str(fibonacci_sum(n)[-1])[-1])
