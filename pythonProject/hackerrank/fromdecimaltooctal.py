import math

import numpy as np
def octal(x):
    s=''
    qoutient=0
    while True:
        remainder=x%8
        quotient=math.floor(x/8)
        s+=str(remainder)
        x=quotient
        if x==0:
            break
    s=s[::-1]
    return s
def bin(x):
    s=''
    qoutient=0
    while True:
        remainder=x%2
        quotient=math.floor(x/2)
        s+=str(remainder)
        x=quotient
        if x==0:
            break
    s=s[::-1]
    return s
def x(n):
    width=len('{0:b}'.format(n))
    for x in range(1,n+1):
        print("{0:{width}b}".format(x,width=width))
        ln=len('{0:b}'.format(x))
        print('{0:{len}b}'.format(x,len=ln))
def print_rangoli(size):
    # your code goes here
    lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    given=lst[:size+1]
    lenght=size*2-1
    c=[[]]*lenght
    width=lenght+math.ceil((size*2-2)/2)*2
    for i in range(lenght):
        for j in range(width):
            c[i].append('-')
    print(c)
def goal(start,end,index,center,given,m):
    center1 = center
    center2 = center
    for y in range(start, end):
        center1 = center1 + 2
        center2 = center2 - 2
        m[y][center1] = given[index]
        m[y][center2] = given[index]
        m[y][center] = given[index-1]
def matrix(size):
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    given = lst[:size]
    given=given[::-1]
    lenght = size * 2 - 1
    width = lenght + math.ceil((size * 2 - 2) / 2) * 2
    m=np.zeros((lenght,width),dtype='str')
    # for x in range(len(m)):
    #     center=
    center=math.floor(width/2)
    # m[0][center]=given[0]
    # print(m[0])
    # m[1][center-2]=given[0]
    # m[1][center+2]=given[0]
    # m[1][center] = given[1]
    # print(m)
    center1=center
    center2=center
    for x in range(size):
        m[x][center]=given[x]
        if x==0:
            continue
        else:
            center1 = center1 + 2
            center2 = center2 - 2
            m[x][center1] = given[0]
            m[x][center2] = given[0]
            m[x][center] = given[x]
    center1 = center
    center2 = center
    for y in range(2,5):
        center1 = center1 + 2
        center2 = center2 - 2
        m[y][center1] = given[1]
        m[y][center2] = given[1]
    center1 = center
    center2 = center
    for y in range(3,5):
        center1 = center1 + 2
        center2 = center2 - 2
        m[y][center1] = given[2]
        m[y][center2] = given[2]
    center1 = center
    center2 = center
    for y in range(4,5):
        center1 = center1 + 2
        center2 = center2 - 2
        m[y][center1] = given[3]
        m[y][center2] = given[3]
    print(m)


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
s=size(20)
print(s)



