class Node:
    def __init__(self, data, left,right):
        self.data = data
        self.left=left
        self.right=right
class tree:
    def __init__(self):
        self.root=None
    def addleft_Node(self,data,node):
        new=Node(data,None,None)
        if self.root is None:
            self.root=new
        else:
            if node.left is not None:
                print('this node is occupied')
                return
            node.left=new
    def addright_Node(self,data,node):
        new = Node(data, None, None)
        if self.root is None:
            self.root = new
        else:
            if node.right is not None:
                print('this node is occupied')
                return
            node.right = new
    def traversal(self,myroot):
        if myroot is None:
            return
        else:
            print(myroot.data)
            self.traversal(myroot.left)
            self.traversal(myroot.right)
tree=tree()
tree.addright_Node(10,tree.root)
tree.addright_Node(12,tree.root)
tree.addright_Node(13,tree.root)
tree.traversal(tree.root)


