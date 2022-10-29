c=[2,4,5,1,3,9,6]

def bubble_sort(c):
    length=len(c)
    for x in range(1,length):
        for m in range(0,len(c)-1):
            if c[m]>c[m+1]:
                temp=c[m]
                c[m]=c[m+1]
                c[m+1]=temp
            else:
                continue
    return c
print(bubble_sort(c))

