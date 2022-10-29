import math


def binary_search_duplicate(lst,low,high,goal):
    if low > high:
        return False
    else:
        mid=math.floor(low+(high-low)/2)
        if lst[mid]== goal:
            if lst[mid-1]==goal:
                if mid-1==0:
                    return mid-1
                return binary_search_duplicate(lst,low,mid,goal)
            else:
                return mid
        elif lst[mid]>goal:
            return binary_search_duplicate(lst,low,mid-1,goal)
        else:
            return binary_search_duplicate(lst,mid+1,high,goal)
lst=[2,4,4,4,7,7,7,9]
goal=7
print(binary_search_duplicate(lst,0,len(lst)-1,goal))