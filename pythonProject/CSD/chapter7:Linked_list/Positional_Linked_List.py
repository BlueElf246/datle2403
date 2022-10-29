from Doubly_link_list import _DoublyLinkedBase
class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container=container
            self._node=node
        def element(self):
            return self._node.element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            return not (self==other)
    def _validate(self,p):
        if not isinstance(p, self.Position):
            return 'must be same type'
        if p._container is not self:
            return 'p not belong to this'
        if p._node.element is None:
            return 'False'
        return p._node
    def _make_position(self,node):
        #return position from a node
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
    def first(self):
        # return 1st position of the list
        return self._make_position(self._header.next)
    def last(self):
        return self._make_position(self._trailer.prev)
    def before(self,p):
        #return the position before p
        node=self._validate(p)
        return self._make_position(node.prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node.next)
    def __iter__(self):
        cursor=self.first()
        while cursor is not None:
            yield cursor.element()
            cursor=self.after(cursor)
    def _insert_between(self,e,prev, next):
        node=super().insert_between(e,prev,next)
        return self._make_position(node)
    def add_first(self,e):
        node=self._insert_between(e, self._header, self._header.next)
        return node
    def add_last(self,e):
        node=self._insert_between(e,self._trailer.prev,self._trailer)
        return node
    def add_before(self,p,e):
        node= self._insert_between(e,self._validate(p).prev, self._validate(p))
        return node
    def add_after(self,p,e):
        node=self._insert_between(e, self._validate(p),self._validate(p).next)
        return node
    def delete(self,p):
        ans=self.delete_node(self._validate(p))
        return ans
    def replace(self,p,e):
        node=self._validate(p)
        old_e=node.element
        node.element=e
        return old_e




