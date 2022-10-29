class MyTree:
    class Node:
        def __init__(self,data, pleft, pright):
            self.data=data
            self._pleft=pleft
            self._pright=pright
    def __init__(self):
        self._root=None
    def is_empty(self):
        return self._root==None
    def addLeftOfTNode(self,data,leafnode):
        node=self.Node(data,None, None)
        if self.is_empty():
            self._root=node
        else:
            leafnode._pleft=node
    def addRightOfNode(self, data, leafnode):
        node = self.Node(data, None, None)
        if self.is_empty():
            self._root = node
        else:
            leafnode._pright = node
    def traversalNLR_preorder(self,myroot):
        if (myroot==None):
            return
        else:
            print(myroot.data)
            self.traversalNLR_preorder(myroot._pleft)
            self.traversalNLR_preorder(myroot._pright)
    def traversal_LNR_inorder(self, myroot):
        if myroot==None:
            return
        else:
            self.traversal_LNR_inorder(myroot._pleft)
            print(myroot.data)
            self.traversal_LNR_inorder(myroot._pright)
    def traversal_LRN_postorder(self, myroot):
        if myroot==None:
            return
        else:
            self.traversal_LRN_postorder(myroot._pleft)
            self.traversal_LRN_postorder(myroot._pright)
            print(myroot.data)
tree=MyTree()

tree.addLeftOfTNode(8, None)
tree.addRightOfNode(10, tree._root)
tree.addLeftOfTNode(5, tree._root)
tree.addLeftOfTNode(1, tree._root._pleft)
tree.addRightOfNode(3, tree._root._pleft)
tree.addLeftOfTNode(9, tree._root._pleft._pright)

#tree.traversalNLR_preorder(tree._root)
tree.traversal_LRN_postorder(tree._root)




