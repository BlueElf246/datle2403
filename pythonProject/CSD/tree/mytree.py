import tnode

class MyTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        if self._root == None:
            return True
        return False

    def addLeftOfTNode(self, new_data, leafNode):
        new_item = tnode.TNode(new_data, None, None)
        if(self.is_empty()):
            self._root = new_item
        else:
            leafNode._pLeft = new_item
    def addRightOfNode(self, new_data, leafNode):
        new_item = tnode.TNode(new_data, None, None)
        if(self.is_empty()):
            self._root = new_item
        else:
            leafNode._pRight = new_item

    def travelsalNLR(self, myroot):
        if(myroot == None):
            return
        print(myroot._data)
        self.travelsalNLR(myroot._pLeft)
        self.travelsalNLR(myroot._pRight)