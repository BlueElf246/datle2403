class _Node:
    def __init__(self, data, prev, next):
        self._data = data
        self._next = next
        self._prev = prev

    def display(self):
        print(self._data)
        print(self._next)
        print(self._prev)