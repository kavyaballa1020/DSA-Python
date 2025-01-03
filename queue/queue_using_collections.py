from collections import deque

queue=deque()

#Enqueue Operation
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

#Displaying
print(queue)

#Dequeue Operation
queue.popleft()
print(queue)

#peek
front=queue[0]
print("Peek element : ",front)