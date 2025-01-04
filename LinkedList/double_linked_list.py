class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        newnode = Node(data)
        if self.head is None:  
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
    
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:  
            self.head = newnode
            return
        temp = self.head
        while temp.next: 
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
        
    def delete_at_begin(self):
        if self.head is None: 
            print("List is empty")
            return
        if self.head.next is None:  
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
    
    def delete_at_end(self):
        if self.head is None:  
            print("List is empty")
            return
        if self.head.next is None:  
            self.head = None
            return
        temp = self.head
        while temp.next: 
            temp = temp.next
        temp.prev.next = None
        
    def display_forward(self):
        if self.head is None:  
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
        
    def display_backward(self):
        if self.head is None:  
            print("List is empty")
            return
        temp = self.head
        while temp.next: 
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
        
dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Forward Traversal:")
dll.display_forward()  

print("Backward Traversal:")
dll.display_backward()  

dll.delete_at_begin()
print("After deleting from beginning:")
dll.display_forward() 

dll.delete_at_end()
print("After deleting from end:")
dll.display_forward()  
