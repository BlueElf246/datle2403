#merge two ordered list into 1 ordered list
def merge_sort(L1,L2):
    new_L=[]
    n=0
    while len(L1)!=0 or len(L2)!=0:
        val1=L1[n]
        val2=L2[n]
        if val1< val2:
            new_L.append(val1)
            L1.remove(val1)
            if len(L1)==0:
                new_L.append(L2)
                break
        else:
            new_L.append(val2)
            L2.remove(val2)
            if len(L2)==0:
                new_L.append(L1)
                break
    return new_L
L1=[2,3,5,6]
L2=[1,4]
print(merge_sort(L1,L2))

