import ctypes
class Dynamic_array:
    def __init__(self):
        self._n=0#count actual element
        self._capacity=1# default array capacity
        self.A=self._make_array(self._capacity)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        #return element at index k
        return self.A[k]
    def append(self,obj):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self.A[self._n]=obj
        self._n+=1
    def _resize(self,c):
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self.A[k]
        self.A=B
        self._capacity=c
    def _make_array(self,c):
        return (c*ctypes.py_object)()
    def insert(self,l,obj):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        for x in range(self._n,l,-1):
            self.A[x]=self.A[x-1]
        self.A[l]=obj
        self._n+=1
    def pop(self,l):
        for m in range(0,self._n):
            if self.A[m]==l:
                for x in range(m,self._n-1):
                    self.A[x]=self.A[x+1]
                self.A[self._n-1]=None
                self._n-=1
                return
array=Dynamic_array()

for x in range(array._n):
    print(array[x])



