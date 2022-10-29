import math
def size(size):
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    result=''
    given = lst[:size]
    given = given[::-1]
    lenght = size * 2 - 1
    width = lenght + math.ceil((size * 2 - 2) / 2) * 2
    for x in range (size+1):
        g=given[:x]
        if x==0:
            continue
        if len(g)==1:
            g = ''.join(g)
            result+=g.center(width,'-')+'\n'
            continue
        else:
            l=g[:x-1]
            l=l[::-1]
            g=g+l
            g='-'.join(g)
            result += g.center(width, '-')+'\n'
    for x in range(size-1,0,-1):
        g = given[:x]
        if len(g) == 1:
            g = ''.join(g)
            result += g.center(width, '-')+'\n'
            continue
        else:
            l = g[:x - 1]
            l = l[::-1]
            g = g + l
            g = '-'.join(g)
            result += g.center(width, '-')+'\n'
    return result
s=size(26)
print(s)