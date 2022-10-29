class Binary_SearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            # insert in left substree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_SearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_SearchTreeNode(data)
            # add in right subtree
    def in_order_traversal(self): #LNR
        element=[]
        if self.left:
            element+=self.left.in_order_traversal()
        # visit base node
        element.append(self.data)
        if self.right:
            element+=self.right.in_order_traversal()
        return element

    def pre_order_traversal(self):
        element=[]
        element.append(self.data)
        # visit left node
        if self.left:
            element+=self.left.pre_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()
        return element
    def post_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.post_order_traversal()
        if self.right:
            element+=self.right.post_order_traversal()
        element.append(self.data)
        return element

        # visit base node
    def search(self,val):
        if self.data == val:
            return True
        elif self.data > val:
            # value in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        elif self.data < val:
            # value in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right:
            return self.right.find_max()
        elif self.right is None:
            max=self.data
            return max
    def find_min(self):
        if self.left:
            return self.left.find_min()
        elif self.left is None:
            min=self.data
            return min
    def calculate_sum(self):
        sum=0
        for x in self.in_order_traversal():
            sum+=x
        return sum
    def delete_node(self,val):
        if self.data >val:
            if self.left:
                self.left=self.left.delete_node(val)
        elif self.data < val:
            if self.right:
                self.right= self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete_node(min_val)
        return self
def build():
    number=[17,4,1,20,9,88,23,18,34,19,17]
    root=Binary_SearchTreeNode(number[0])
    for x in range(1,len(number)):
        root.add_child(number[x])
    # print(root.in_order_traversal())
    # print(root.search(20))
    # print(root.find_max())
    # print(root.find_min())
    # print(root.calculate_sum())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())

tree=Binary_SearchTreeNode(10)
tree.add_child(9)
tree.add_child(11)
tree.delete_node(10)
print(tree.in_order_traversal())