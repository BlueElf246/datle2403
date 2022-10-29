import matplotlib.pyplot as plt
import numpy as np
def x(n):
    v=0
    for i in range(20**n):
        v+=i
    return v
data=np.array([2,3,4,5,6],dtype='int64')
size=20**data
print(size)
from time import time
s=dict()
for n in range(2,7):
    start=time()
    x(n)
    stop=time()
    result=(stop-start)
    s[n]=result
print(s)
x_axis=list(s.keys())
y_axis=list(s.values())
# fig=plt.figure(figsize=(10,5))
plt.plot(x_axis,y_axis,marker='D',color='r')
plt.legend()
plt.show()

