class ArrayStack:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def push(self,obj):
        self.data.append(obj)
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
         return self.data.pop()
    def top(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.data[-1]
    def __getitem__(self, item):
        return self.data[item]
def run1():
    stack=ArrayStack()
    print(stack.pop())
    stack.push(12)
    stack.push(22)
    print(stack[0])
    print(stack.pop())
    for x in stack:
        print(x)


