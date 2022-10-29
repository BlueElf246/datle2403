file=open('file_test.txt', 'r')
new=file.read()
def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1
    return list_a
m=''
new=new.replace(',',' ').replace(':',' ').replace('.',' ').replace('"',' ').replace('[',' ').replace(']',' ').replace('(',' ').replace(')',' ').replace('-','')
for x in new:
    if x.isdigit():
        continue
    else:
        x=x.lower()
        m+=x
m=m.split(' ')
eng=dict()
for x in m:
    x=x.strip()
    if x=='':
        continue
    eng[x]=eng.get(x,0)+1
lst=list(eng.items())
lst_1=[(x) for y,x in lst]
n=insertion_sort(lst_1)
x=n[::-1][0:5]
l=list()
for key,value in eng.items():
    for m in x:
        if value==m:
            l.append((key,value))
            continue
l2=[(x,y) for y,x in l]
l3=insertion_sort(l2)
for x in l3[::-1]:
    print(x)


