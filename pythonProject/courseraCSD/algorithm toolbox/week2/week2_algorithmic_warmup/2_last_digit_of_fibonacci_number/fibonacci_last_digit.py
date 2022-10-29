# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    F=list()
    F.append(0)
    F.append(1)
    for x in range(2,n+1):
        F.append(F[x-1]+F[x-2])
    return F[-1]%10
if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
