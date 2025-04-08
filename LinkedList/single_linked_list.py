class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singly_linked_list:
    def __init__(self):
        self.head=None
        self.size=0
            
    def insert_at_end(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        self.size+=1
        
    def insert_at_beginning(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        self.size+=1
    
    def delete_at_begin(self):
        if self.head==None:
            print("List is empty")
        self.head=self.head.next
        self.size-=1
    def delete_at_end(self):
        if self.head==None:
            print("List is empty")
        temp=self.head
        while temp.next and temp.next.next:
            temp=temp.next
        temp.next=None
        self.size-=1
    def posInsert(self,data,pos):
        if pos>self.size+1 or pos<1:
            print("Invalid")
            return
        newnode=node(data)
        temp=self.head
        i=1
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            self.size+=1
            return
        while i<pos-1:
            temp=temp.next
            i+=1
        newnode.next=temp.next
        temp.next=newnode
        self.size+=1
    def posDelete(self,pos):
        if pos<1 or pos>self.size:
            print("Invalid")
            return
        if pos==1:
            self.head=self.head.next
            self.size-=1
            return
        temp=self.head
        i=1
        while i<pos-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        self.size-=1
        
        
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
l.display()
l.insert_at_end(30)
l.insert_at_end(40)
l.display()
l.delete_at_begin()
l.display()
l.delete_at_end()
l.display()
l.posInsert(80,4)
l.display()
l.posDelete(1)
l.display()