import mytree as t
tree = t.MyTree()

tree.addLeftOfTNode(8, None)
tree.addLeftOfTNode(5, tree._root)
tree.addRightOfNode(10, tree._root)
tree.addLeftOfTNode(1, tree._root._pLeft)
tree.addRightOfNode(3, tree._root._pLeft)
tree.addLeftOfTNode(9, tree._root._pLeft._pRight)
tree.addLeftOfTNode(4,tree._root._pRight)
tree.addRightOfNode(20, tree._root._pRight)
tree.addLeftOfTNode(7,tree._root._pRight._pLeft)

tree.travelsalNLR(tree._root)