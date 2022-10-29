def reverse_array(lst,start,stop):
    print(start,stop)
    if start > stop:
        return lst
    else:
        temp=lst[start]
        lst[start]=lst[stop]
        lst[stop]=temp
        return reverse_array(lst,start+1,stop-1)
lst=[1,2,3,4,5,6,7]
f=reverse_array(lst,0,len(lst)-1)
print(f)