class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class circular_linked_list:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            newnode.next=self.head
            self.head=newnode
            temp.next=self.head
        
    def insert_at_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!= self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
        
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
        
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp=self.head
            while temp.next.next !=self.head:
                temp=temp.next
            temp.next=self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp=self.head
            while temp.next != self.head:
                print(temp.data,end=" --> ")
                temp=temp.next
            print(temp.data)

cll=circular_linked_list()

cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.insert_at_end(40)

print("Circular Linked List:")
cll.display()  

cll.delete_at_begin()
print("After deleting from beginning:")
cll.display()  

cll.delete_at_end()
print("After deleting from end:")
cll.display()  