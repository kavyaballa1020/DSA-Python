class simple_queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.rear=-1
        self.front=-1
        
    def enqueue(self,data):
        if self.rear==self.size-1:
            print("Queue is full")
        elif self.front==-1:
            self.front=0
        self.rear=self.rear+1
        self.queue[self.rear]=data
    
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("Underflow")
        print("Dequeued element is ",self.queue[self.front])
        self.front=self.front+1 
    
    def peek(self):
        if self.front==-1 and self.rear==-1:
            print("Underflow")
        print("peek element is : ",self.queue[self.front])

    def isempty(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")
        
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.queue[self.front:self.rear+1])
queue=simple_queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.peek()
queue.display()