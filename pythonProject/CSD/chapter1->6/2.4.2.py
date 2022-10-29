
class Progression():
    def __init__(self,starting_value=0):
        self._current=starting_value
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            self._advance()
            return self._current
    def __iter__(self):
        return self
    def _advance(self):
        self._current+=1
    def print_progression(self,n):
        print(' '.join(str(next(self)) for i in range(n)))
class ArithmeticProgression(Progression):
    def __init__(self,const=1,start=0):
        super().__init__(start)
        self.const=const
    def _advance(self):
        self._current+=self.const
class GeometricProgression(Progression):
    def __init__(self,const=1,start=0):
        super().__init__(start)
        self.const=const
    def _advance(self):
        self._current *= self.const
class FibonacciProgression(Progression):
    def __init__(self,start_1=0,start_2=1):
        super().__init__(start_1)
        self.start_2=start_2
    def _advance(self):
        temp=self.start_2
        self.start_2=self._current+self.start_2
        self._current=temp

m=ArithmeticProgression(start=0,const=2)
m.print_progression(10)




