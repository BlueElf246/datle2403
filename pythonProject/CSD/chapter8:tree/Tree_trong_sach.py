class Tree:
    class Position:
        def element(self):
            raise NotImplementedError
        def __eq__(self, other):
            raise  NotImplementedError
        def __ne__(self, other):
            return not (self ==other)
    def root(self):
        raise NotImplementedError
    def parent(self,p):
        raise  NotImplementedError
    def num_children(self,p):
        raise NotImplementedError
    def children(self,p):
        raise NotImplementedError
    def __len__(self):
        raise NotImplementedError
    def is_root(self,p):
        return self.root()==p
    def is_leaf(self,p):
        return self.num_children(p)==0
    def is_empty(self):
        return len(self)==0
    def depth(self,p):
        if self.is_root(p)==0:
            return 0
        else:
            return 1+self.depth(self.parent(p)) # recursively +1 until reach the root, compute depth of current position
    # def _height1(self,p): # compute the height of a tree
    #     return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    def _height2(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height2(c) for c in self.children(p))
    def height(self,p=None):
        if p is None:
            p=self.root()
        return self._height2(p)
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError
    def right(self,p):
        raise NotImplementedError
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self,p): #return children of parent node
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element','_parent','_left','_right'
        def  __init__(self, element, parent=None,left=None, right=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            #return true if other is a Position representing the same location
            return type(other) is type(self) and other._node is self._node
    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError
        if p._container is not self:
            raise ValueError
        if p._node._parent is p._node:
            raise ValueError
        return p._node
    def _make_position(self,node):
        #return position instance for given node
        return self.Position(self,node) if node is not None else None
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
        return self._make_position(self._root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):# return number of childern at pos p
        node=self._validate(p)
        count=0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
        return count
    def _add_root(self,e):
        #Place element e at the root of an empty tree and return new Position.
        if self._root is not  None: raise ValueError
        self._size=1
        self._root=self._Node(e)
        return self._make_position(self._root)
    def _add_left(self,p,e):
        #Create a new left child for Position p, storing element e, Return the Position of new node
        node=self._validate(p)
        if node._left is not  None: raise ValueError
        self._size+=1
        node._left=self._Node(e,node)
        return self._make_position(node._left)
    def _add_right(self,p,e):
        #Create a new right child for Position p, storing element e, Return the Position of new node
        node=self._validate(p)
        if node._right is not  None: raise ValueError
        self._size+=1
        node._left=self._Node(e,node)
        return self._make_position(node._right)
    def _replace(self,p,e):
        #Replace the element at position p with e, and return old element.
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        #Delete the node at Position p, and replace it with its child, if any, Return the element that had been stored at Position p.
        node=self._validate(p)
        if self.num_children(p)==2:raise ValueError
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent # child's grandparent becomes parent
        if child is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1
        node._parent=node
        return node._element

    def   _attach(self, p, t1, t2):
        #Attach trees t1 and t2 as left and right subtrees of external p.
        node=self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf ')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size+=len(t1)+len(t2)
        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not  t2.is_empty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0

tree=LinkedBinaryTree()
tree._add_root(10)
tree._add_left(tree.root(),11)
tree._add_right(tree.root(),12)
tree._add_right(tree.left(tree.root()),14)
print(tree.right(tree.left(tree.root())).element())




