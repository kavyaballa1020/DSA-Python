class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self):
        self.root=None

    def binary_tree_insertion(self):
        data=int(input("Enter data or -1 for no node"))
        if data==-1:
            return None
        
        newnode=Node(data)
        print(f"enter left child of the {data}")
        newnode.left=self.binary_tree_insertion()
        print(f"enter right child of the {data}")
        newnode.right=self.binary_tree_insertion()
        
        return newnode

    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
    def levelorder(self,root):
        if not root:
            return
        queue=[root]
        while queue:
            size=len(queue)
            for i in range(size):
                 current=queue.pop(0)
                 print(current.data,end=" ")
                 if current.left:
                     queue.append(current.left)
                 if current.right:
                     queue.append(current.right)
                    
tree=BinaryTree()
tree.binary_tree_insertion()
tree.preorder(tree.root)
tree.postorder(tree.root)      
tree.inorder(tree.root)      
tree.levelorder(tree.root)      
      
                 