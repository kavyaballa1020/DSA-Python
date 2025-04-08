class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert_at_beginning(self, data):
        newnode = Node(data)
        if self.head is None:  
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        self.size+=1
    
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
        self.size+=1
        
    def delete_at_begin(self):
        if self.head is None: 
            print("List is empty")
            return
        if self.head.next is None:  
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
        self.size-=1
    
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
        self.size-=1
    
    def posInsert(self,data,pos):
        if pos>self.size+1 or pos<1:
            print("Invalid")
            return
        newnode=Node(data)
        temp=self.head
        i=1
        if pos==1:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            self.size+=1
            return
        while i<pos-1:
            temp=temp.next
            i+=1
        newnode.next=temp.next
        newnode.prev=temp
        temp.next.prev = newnode
        temp.next=newnode
        self.size+=1
    def posdelete(self,pos):
        if pos<1 or pos>self.size:
            print("Invalid")
            return
        if pos==1:
            self.head=self.head.next
            self.head.prev=None
            self.size-=1
            return
        temp=self.head
        i=1
        while i<pos-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        temp.next.prev = temp
        self.size-=1
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
dll.display_forward()
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.display_forward()

print("Forward Traversal:")
dll.display_forward()  
print("Backward Traversal:")
dll.display_backward()  

dll.delete_at_begin()
dll.display_forward() 
dll.delete_at_end()
dll.display_forward() 

dll.posInsert(25, 3)
dll.display_forward()

dll.posdelete(1)
dll.display_forward()