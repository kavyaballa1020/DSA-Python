class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class queue:   
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data
    
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print() 
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
print("Dequeued element : ",q.dequeue())
q.display()
print("peek element : ",q.peek())
