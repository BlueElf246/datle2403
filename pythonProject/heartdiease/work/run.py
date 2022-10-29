lst=[]
for x in range(100):
    for y in range(100):
        r=3*x+5*y
        lst.append(r)
lst.sort()
m=set(lst)
l=list(m)
for x in range(len(l)):
    if l[x+1]-l[x]>1:
        print(l[x])
