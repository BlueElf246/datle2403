class Tree_Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent= self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            p=p.parent
            level+=1
        return level
    def print_tree(self):
        space='-'*self.get_level()
        print(space,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
tree=Tree_Node('laptop')
mac=Tree_Node('macbook')
mac.add_child(Tree_Node('air'))
mac.add_child(Tree_Node('pro'))

tree.add_child(mac)
tree.add_child(Tree_Node('samsung'))
print(mac.get_level())
