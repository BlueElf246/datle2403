# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    pointss=set()
    minimum_right_endpoint=1000
    total=[]
    for x in segments:
        if minimum_right_endpoint> x[-1]:
            minimum_right_endpoint=x[-1]
    points.append(minimum_right_endpoint)
    for w in segments:
        temp=[]
        for x in range(w[0],w[-1]+1):
            temp.append(x)
        total.append(temp)
    t=False
    while True:
        while t==False:
            for x in range(0,len(total)):
                if minimum_right_endpoint in total[x]:
                    total.remove(total[x])
                    pointss.add(minimum_right_endpoint)
                    t=False
                    if len(total)==0:
                        t=True
                    break
                else:
                    t=True
        if len(total)==0:
            return pointss
        else:
            minimum_right_endpoint = 1000
            for k in total:
                if minimum_right_endpoint > k[-1]:
                    minimum_right_endpoint = k[-1]
            t=False
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
