def linearsum(lst,end):
    if end==0:
        return lst[end]
    else:
        if end==1:
            return linearsum(lst,end-1)
        return lst[end-1]+linearsum(lst,end-1)
lst=[1,2,3,4,5,4,9]
s=linearsum(lst,end=4)
print(s)