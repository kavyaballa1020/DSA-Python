from queue import Queue
q=Queue()

#adding elements to the queue
q.put(12)
q.put(13)
q.put(14)
q.put(15)
q.put(16)

#Displaying the size elements
print(q.qsize())

#Dequeue elements
dequeued=q.get()
print("Dequeue element",dequeued)
print(q.qsize())


isempty=q.empty()
print("isEmpty : ",isempty)
