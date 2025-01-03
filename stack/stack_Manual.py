class stack_manual:
    def __init__(self,size):
        self.stack=[None]*size
        self.size=size
        self.top=-1
        
    def push(self,data):
        if self.top==self.size-1:
            print("overflow")
        self.top=self.top+1;
        self.stack[self.top]=data 
    
    def pop(self):
        if self.top==-1:
            print("Underflow")
        print("Popped element is ",self.stack[self.top])
        self.top=self.top-1
        
    def peek(self):
        if self.top==-1:
            print("Underflow")
        print("Peek element is : ",self.stack[self.top])
        
    def isempty(self):
        if self.top==-1:
            print("stack is empty")
    
    def dispaly(self):
        print("Displaying elements : ",self.stack[:self.top+1])
        
stack = stack_manual(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.peek()
stack.dispaly()