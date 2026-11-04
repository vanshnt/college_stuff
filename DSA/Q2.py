# Q. 2 Write a program to perform the following operations on a Linear Queue
# 1. Enqueue an element into the queue
# 2. Dequeue an element from the queue
# 3. Display


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.rear = None
#         self.front = None

#     def enqueue(self,data):
#         NewNode = Node(data)
#         if self.rear is None:
#             self.rear = self.front = NewNode
#         else:
#             self.rear.next = NewNode
#             self.rear = NewNode
#     def dequeue(self):
#         if self.front is None:
#             print("Queue is empty")
#             self.rear = None
#             return
#         else:
#             curr = self.front
#             print("Deleted Node: ",curr.data)
#             self.front = curr.next
#     def printqueue(self):
#         curr = self.front
#         while curr:
#             print(curr.data,end=" ")
#             curr = curr.next
#         print()

# q = Queue()
# q.enqueue(5)
# q.enqueue(10)
# q.enqueue(15)
# q.enqueue(20)
# q.printqueue()

# q.dequeue()
# q.dequeue()
# q.printqueue()

# 4. Reverse the queue using stack

# queue = [10,20,30,40,50]
# stack = []
# print("Initial Queue: ", queue)
# while len(queue) > 0:
#     stack.append(queue.pop(0))
# while len(stack) > 0:
#     queue.append(stack.pop())
# print("Reversed Queue:",queue)


# 5. Merge two queues into one.

# q1 = [10, 20, 30]
# q2 = [40, 50, 60]
# print("First Queue: ", q1)
# print("Second Queue: ", q2)
# q3 = []

# while len(q1) > 0:
#     q3.append(q1.pop(0))

# while len(q2) > 0:
#     q3.append(q2.pop(0))

# print("Merged Queue:", q3)




# 6. Check if two queues are identical


q1 = [11, 12, 13, 14]
q2 = [11, 12, 13, 14]
if len(q1) != len(q2):
    print("Queues are not identical")
else:
    identical = True
    for i in range(len(q1)):
        if q1[i] != q2[i]:
            identical = False
            break
    if identical:
        print("Queues are identical")
    else:
        print("Queues are not identical")

