class Queues:
    def __init__(self):
        self.lst=[]
        self.index=0
    def enqueues(self,value):
        self.lst.append(value)
    def dequeues(self):
        if self.is_empty():
             return None
        self.lst[self.index]=None
        self.index+=1
    def first(self):
        if self.is_empty():
             return None
        return self.lst[self.index]
    def last(self):
        if self.is_empty():
             return None
        return self.lst[-1]
    def is_empty(self):
        if len(self.lst)==0:
            return True
        return False
k=Queues()
k.enqueues(4)
k.enqueues(10)
k.dequeues()
print(k.first())
print(k.lst)