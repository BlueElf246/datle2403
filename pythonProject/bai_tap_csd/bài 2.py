from array_stack_class import ArrayStack
arr=ArrayStack()
import math
def run(x,base):
    m=x
    while math.floor(m)!=0:
        r= m % base
        arr.push(r)
        m=math.floor(m/base)
run(123,2)
s=''
for x in range(len(arr)):
    k=arr.pop()
    s+=str(k)
print(s)

