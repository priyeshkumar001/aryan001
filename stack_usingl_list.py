# Stack using list
stack = []

# Push elements into stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print("Stack after push operations:", stack)

# Pop element from stack
removed = stack.pop()
print("Popped element:", removed)

print("Stack after pop operation:", stack)

# Peek (top element)
top = stack[-1]
print("Top element of stack:", top)

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")