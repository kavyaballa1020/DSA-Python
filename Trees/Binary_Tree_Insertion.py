class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        data = int(input("Enter data (-1 for no node): "))
        if data == -1:
            return None

        new_node = Node(data)

        print(f"Enter left child of {data}:")
        new_node.left = self.insert()

        print(f"Enter right child of {data}:")
        new_node.right = self.insert()

        return new_node

    def preorder(self, root):
        if root:
            print(root.data, end=" --> ")
            self.preorder(root.left)
            self.preorder(root.right)

# Driver Code
if __name__ == "__main__":
    tree = BinaryTree()

    print("Start building the binary tree:")
    tree.root = tree.insert()

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)