import math


def binary_find_max(lst,low,high,max=0):
    if low==high:
        return lst[low]
    else:
        m=math.floor((low+high)/2)
        max1=binary_find_max(lst,low,m,max)
        max2=binary_find_max(lst,m+1,high,max)
        if max1>max2:
            return max1
        else:
            return max2
print(binary_find_max([5,3,4,10,8,0,1],0,4))
