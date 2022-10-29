# python3
import sys


def compute_min_refills(distance, tank, stops):
    #distance: khoảng cách từ xuất phát đến dích
    #tank: quãng đường tối đa xe có thể đi khi đầy bình
    # stops: list các điểm xăng, cách nơi xuất phát
    curr=0
    stops.insert(0,0)
    lst=[]
    x=0
    while True:
        m=x
        while stops[x+1]-stops[m]<=tank:
            x+=1
            if x+1==len(stops):
                break
        if m==x and stops[x+1]-stops[m]>tank:
            return False
        else:
            lst.append(x)
            if x + 1 == len(stops):
                break
    if distance-stops[lst[-1]]>tank:
        return False
    else:
        for x in lst:
            print(stops[x])
print(compute_min_refills(10,3,[1,2,5,9]))
e=(10,3,[1,2,5,9])
d=(950,400,[200,375,550,750])
# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))
