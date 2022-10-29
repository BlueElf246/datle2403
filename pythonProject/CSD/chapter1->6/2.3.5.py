class Range():
    def __init__(self,start,end,count=0):
        self.start=start
        self.end=end
        self.step=count
        self.lenght=max(0,(self.end-self.start+self.step-1)//self.step)
    def __len__(self):
        return self.lenght
    def __getitem__(self, item):
        if item<0:
            item+=len(self)
        if item >=len(self):
            raise IndexError('index out of rangesss ')
        return self.start + item*self.step
x=Range(1,10,1)
for m in x:
    print(m)