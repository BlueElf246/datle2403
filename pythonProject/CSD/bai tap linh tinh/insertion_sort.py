def insertion_sort(lst):
    for k in range(1, len(lst)):
        j=k
        curr=lst[k]
        while lst[j-1]>curr:#2853
            lst[j]=lst[j-1] #2883
            j-=1
            print(lst)
        lst[j]=curr
    print(lst)
data=[2,8,5,3]
insertion_sort(data)




