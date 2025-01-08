class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertion(self, root, data):
        if root is None:
            return Node(data)  
        if data < root.data:
            root.left = self.insertion(root.left, data)
        elif data > root.data:
            root.right = self.insertion(root.right, data)
        return root  

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

bst = BinarySearchTree()
root = None

elements = [50, 30, 20, 40, 70, 60, 80]

for i in elements:
    root = bst.insertion(root, i)

print("Preorder Traversal:")
bst.preorder(root)