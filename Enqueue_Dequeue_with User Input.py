queue = []

n = int(input("How many elements do you want to add: "))

# Enqueue elements
for i in range(n):
    element = int(input("Enter element: "))
    queue.append(element)

print("Queue elements:", queue)

# Dequeue operation
if len(queue) > 0:
    print("Removed element:", queue.pop(0))
else:
    print("Queue is empty")

print("Queue after dequeue:", queue)