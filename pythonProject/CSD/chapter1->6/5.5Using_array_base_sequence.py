import ctypes
class ScoreBoard:
    def __init__(self,capacity=10):
        self.board= [None]*capacity
        self.n=0
    def __getitem__(self, item):
        return self.board[item]
    def __str__(self):
        return '\n'.join(str(self.board[j]) for j in range(self.n))
    def add(self,entry):
        score=entry.get_score()
        good=self.n < len(self.board) or score> self.board[-1].get_score() #good is true if number of element < capacity
        # or new_score > the last score(the lowest score)
        if good:
            if self.n < len(self.board):
                self.n+=1
            j=self.n-1
            while j>0 and self.board[j-1].get_score() <score:
                self.board[j]=self.board[j-1]
                j-=1
            self.board[j]=entry


class GameEntry:
    def __init__(self,name,score):
        self.name=name
        self._score=score
    def get_name(self):
        return self.name
    def get_score(self):
        return self._score
    def __str__(self):
        return (f'{self.name}, {self._score}')
dat=GameEntry('dat',12)
ScoreBoard=ScoreBoard()
ScoreBoard.add(dat)
print(ScoreBoard[0])

