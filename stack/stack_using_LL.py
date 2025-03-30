class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    
    def display(self):
        if self.is_empty():
            return "Stack is empty"
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print("Popped element : ",s.pop())
s.display()
print("peek element : ",s.peek())
