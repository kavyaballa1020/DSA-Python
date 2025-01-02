from collections import deque
stack=deque()

#push elements
stack.append(10)
stack.append(20)
stack.append(30)

#display elements
print(stack)

#pop elements
stack.pop()
print(stack)

#peek elements
peek=stack[-1]
print(peek)

