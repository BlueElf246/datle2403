from ddl import doubly_linked_list
class doublehashtable:
    def __init__(self, tablesize = 10):
        self.ts = tablesize
        self.List = [None]*self.ts
        self.count = 0

    def LargestPrime(self):
        largest = 0
        for x in range(self.ts, 1, -1):
            c = True
            for y in range(2, x):
                if x % y == 0:
                    c = False
                    break
            if c == True:
                return x
    def hash1(self, key):
        return key % self.ts

    def hash2(self, key):
        return self.LargestPrime() - key % self.LargestPrime()

    def doublehashing(self, key):
            comp = False
            i = 0
            while not comp:

                index = (self.hash1(key) + i * self.hash2(key)) % self.ts  # Index = ( HashFunc1 - i*HashFunc2)%TABle_SIZE

                if self.List[index] == None:
                    self.List[index] = doubly_linked_list()
                    self.List[index].add_head(key)
                    comp = True
                    self.count += 1
                else:
                    if self.count==self.ts:
                        self.List[index].add_tail(key)
                        comp = True
                    else:
                        i += 1
            return self.List

    def PrintHashList(self):
        for i in range(0, len(self.List)):
            print(self.List[i].traversal())

    def is_empty(self):
        k = []
        for x, y in enumerate(self.List):
            if y is None:
                k.append(x)
        print(f'cac index chua co gia tri la {k}')

    def check(self,index):
        m=self.List[index]
        if m is not None:
            print(f'cac gia tri trong index {index} la {m.traversal()}')

tableSize = 10  # Taking 5 as size of the hash Table
DHash = doublehashtable(tableSize)

InputElements = [100,25,16,19,21,50,66,70,82,44,46,99,78,86]

for i in InputElements:
    print(DHash.doublehashing(i))

DHash.PrintHashList()

print('\n')
print("The Hash List After Entering Elements" )





