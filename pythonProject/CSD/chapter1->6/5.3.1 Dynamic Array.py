import ctypes
class DynamicArray():
    def __init__(self):
        self._n=0 #count actual element
        self._capacity=1 # default capacity
        self._A=self._make_array(self._capacity) # low-level array
    def __len__(self):
        #return number of elements in array
        return self._n
    def __getitem__(self, k):
        #return element at index k
        if not 0<= k < self._n:
            raise IndexError('index invalid')
        else:
            return self._A[k]
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
    def _resize(self,c):
        #resize internal array to capacity c
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A=B
        self._capacity=c
    def insert(self,k,value):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n,k,-1):
            self._A[j]=self._A[j-1]
        self._A[k]=value
        self._n+=1
    def _make_array(self,c):
        #return new array with capacity c
        return (c*ctypes.py_object)()
    def _remove(self,value):
        num=0
        for x in range(self._n):
            if self._A[x]==value:
                num=x
                break
        if num==0:
            raise IndexError('not found')
        else:
            for j in range(num,self._n,-1):
                self._A[j]=self._A[j+1]
            self._n-=1
    def extend(self,list2):
        num=len(list2)
        while num+self._n> self._capacity:
            self._resize(2 * self._capacity)
        else:
            for x in range(0,num):
                self.append(list2[x])
x=DynamicArray()
m=10
for j in range(0,20):
    x.append(m)
    print(f'iter{j}')
    print(x._capacity)
