# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def EuclidGCD(a,b):
    if b==0:
        return a
    aprime= a%b
    return EuclidGCD(b,aprime) # condition a>b, so we swap that a >b
def lcm(a,b):
    gcd=EuclidGCD(a,b)
    lcm=(a*b)/gcd
    return lcm
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

