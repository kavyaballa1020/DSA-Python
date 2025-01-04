class circular_queue:
    def __init__(self,size):
        self.circular_queue=[None]*size
        self.size=size
        self.front=self.rear=-1
    
    def enqueue(self,data):
        if (self.rear+1)%self.size==self.front:
            print("Queue is full")
        elif self.front==-1:
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size
        self.circular_queue[self.rear]=data
        
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            print("Deleted Element is : ",self.circular_queue[self.front])
            self.front=(self.front+1)%self.size
    
    def peek(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            print("Peek element is : ",self.circular_queue[self.front])
            
    def display(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            print("Displaying Elements : ",self.circular_queue[self.front:self.rear+1])

queue=circular_queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.peek()
queue.display()