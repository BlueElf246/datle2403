class TNode:
    def __init__(self, data, pLeft, pRight):
        self._data = data
        self._pLeft = pLeft
        self._pRight = pRight

    def display(self):
        print(self._data)
        print(self._pLeft)
        print(self._pRight)