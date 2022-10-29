from Doubly_link_list import _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self._header.next.element
    def last(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self._trailer.next.element
    def insert_first(self,e):
        self.insert_between(e, self._header, self._header.next)
    def insert_last(self,e):
        self.insert_between(e,self._trailer.prev, self._trailer)
    def delete_first(self):
        self.delete_node(self._header.next)
    def delete_last(self):
        self.delete_node(self._trailer.prev)

