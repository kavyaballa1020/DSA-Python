class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Circular_linked_list:
    def __init__(self):
        self.tail= None
        self.size= 0
    def insertBegin(self,data):
        new_node= node(data)
        if self.tail is None:
            self.tail= new_node
            self.tail.next= self.tail
        else:
            new_node.next= self.tail.next
            self.tail.next= new_node
        self.size+= 1
    def insertEnd(self,data):
        new_node= node(data)
        if self.tail is None:
            self.tail= new_node
            self.tail.next= self.tail
        else:
            new_node.next= self.tail.next
            self.tail.next= new_node
            self.tail= new_node
        self.size+= 1
        
    def deleteBegin(self):
        if self.tail is None:
            return
        if self.tail.next== self.tail:
            self.tail= None
        else:
            self.tail.next= self.tail.next.next
        self.size-= 1
        
    def deleteEnd(self):
        if self.tail is None:
            return
        if self.tail.next== self.tail:
            self.tail= None
        else:
            temp= self.tail.next
            while temp.next!= self.tail:
                temp= temp.next
            temp.next= self.tail.next
            self.tail= temp
        self.size-= 1
    
    def posInsert(self,data,pos):
        if pos< 0 or pos> self.size:
            return
        if pos== 0:
            self.insertBegin(data)
        elif pos== self.size:
            self.insertEnd(data)
        else:
            new_node= node(data)
            temp= self.tail.next
            i=1
            while i<pos-1:
                temp= temp.next
                i+=1
            new_node.next= temp.next
            temp.next= new_node
            self.size+= 1
            
    def posDelete(self,pos):
        if pos< 0 or pos>= self.size:
            return
        if pos== 0:
            self.deleteBegin()
        elif pos== self.size-1:
            self.deleteEnd()
        else:
            temp= self.tail.next
            i=1
            while i<pos-1:
                temp= temp.next
                i+=1
            temp.next= temp.next.next
            self.size-= 1
    
    def display(self):
        if self.tail is None:
            return
        temp= self.tail.next
        while temp!= self.tail:
            print(temp.data, end=" -> ")
            temp= temp.next
        print(self.tail.data, end=" ")
        print()
    
    def reverese(self):
        if self.tail is None:
            return
        prev = None
        curr = self.tail.next  
        first = curr          

        while curr != self.tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        next_node = curr.next
        curr.next = prev
        next_node.next = curr  

        self.tail = first     

        
           
c=Circular_linked_list()
c.insertBegin(1)
c.insertBegin(2)
c.insertBegin(3)
c.display()
c.insertEnd(4)
c.insertEnd(5)
c.display()
c.deleteBegin()
c.display()
c.deleteEnd()
c.display()
c.posInsert(6,2)
c.display()
c.posDelete(2)
c.display()
c.reverese()
c.display()