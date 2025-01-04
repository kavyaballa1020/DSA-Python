class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singly_linked_list:
    def __init__(self):
        self.head=None
            
    def insert_at_end(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        
    def insert_at_beginning(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    
    def delete_at_begin(self):
        if self.head==None:
            print("List is empty")
        self.head=self.head.next
    
    def delete_at_end(self):
        if self.head==None:
            print("List is empty")
        temp=self.head
        while temp.next and temp.next.next:
            temp=temp.next
        temp.next=None
    
    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" --> ")
                temp=temp.next
            print()
l=singly_linked_list()
l.insert_at_beginning(10)
l.insert_at_beginning(20)
l.insert_at_end(30)
l.insert_at_end(40)
l.insert_at_beginning(50)
l.display()
l.delete_at_begin()
l.display()
l.delete_at_end()
l.display()