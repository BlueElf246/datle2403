# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10
def partial(m,n):
    F=list()
    F.append(0)
    F.append(1)
    for x in range(2,n+1):
        F.append(F[x-1]+F[x-2])
    sum=0
    for x in range(m,n+1):
        sum+=F[x]
    return str(sum)[-1]
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(partial(from_, to))
