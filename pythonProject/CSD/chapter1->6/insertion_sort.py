def insertion_sort(A):
    for k in range(1,len(A)):
        j=k
        cur=A[k]
        while j>0 and A[j-1]> cur:
            A[j]=A[j-1]
            j-=1
        A[j]=cur
    return A
lst=[2,3,4,1]
print(insertion_sort(lst))