import Dnode


class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head is None:
            return True
        return False


    def addTail(self, new_data):
        new_item = Dnode._Node(new_data, None, None)

        if self.is_empty():
            self._head = new_item
        else:
            self._tail._next = new_item
            self._tail._next._prev = self._tail

        self._tail = new_item

    def addHead(self,new_data):
        new_item = Dnode._Node(new_data, None, None)

        if self.is_empty():
            self._tail = new_item
        else:
            self._head._prev = new_item
            new_item._next = self._head

        self._head = new_item

    def removeTail(self):
        if self.is_empty():
            print('DLL is empty')
            return

        self._tail = self._tail._prev
        self._tail._next = None

        if self.is_empty():
            self._head = None

    def removeHead(self):
        if self.is_empty():
            print('DLL is empty')
            return

        self._head = self._head._next
        self._head._prev = None

        if self.is_empty():
            self._tail = None

    def traversal(self):
        if self.is_empty():
            print("SSL is empty")
            return
        current = self._head
        while current is not None:
            print(current._data)
            current = current._next