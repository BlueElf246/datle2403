# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def sum1(n,su=0):
    if n==1:
        return (1,0,0)
    else:
        a,b,su=sum1(n-1,su)
        su+=a**2
        return (a+b,a,su)
if __name__ == '__main__':
    n = int(stdin.read())
    print(str(sum1(n+1)[-1])[-1])
