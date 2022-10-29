from array_queue import ArrayQueue
lst=['SE01,An,M','SE02,Binh,M','SE03,Lam,F','SE04,Cuong,M','SE05,Tam,M','SE06,Lan,F','SE07,Xuan,F','SE08,Hung,M','SE09,Mai,F']
queue1=ArrayQueue()
for x in lst:
    if x[-1]=='M':
        queue1.enqueue(x)
queue2=ArrayQueue()
for y in lst:
    if y[-1]=='F':
        queue2.enqueue(y)
while  not queue1.is_empty() or not queue2.is_empty():
    if not queue1.is_empty():
        print(queue1.dequeue())
    if  not queue2.is_empty():
        print(queue2.dequeue())
