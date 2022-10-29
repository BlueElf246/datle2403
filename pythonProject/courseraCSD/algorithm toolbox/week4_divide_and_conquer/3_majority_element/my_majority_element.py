import math

lst=[1,2,3,4]
def naive_approach(lst):
    count=1
    for x in lst:
        for y in range(1,len(lst)):
            if x==lst[y]:
                count+=1
        if count > len(lst)/2:
            return x
        else:
            count=0
    return None
def faster_approach(lst,low,high,goal):
    mid=math.floor(low+(high-low)/2)
    new=lst[low:high+1]
    if len(new)==1 and new[0]!=goal:
        return 0
    elif new.count(goal)==len(new):
        return len(new)
    else:
        return faster_approach(lst,low,mid,goal)+faster_approach(lst,mid+1,high,goal)

sett=set(lst)
lenn=math.floor(len(lst)/2)
for x in sett:
    if faster_approach(lst,0,len(lst)-1,x) > lenn:
        print(x)