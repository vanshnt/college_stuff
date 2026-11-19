class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self,data):
        NewNode = Node(data)
        if self.rear is None:
            self.rear = self.front = NewNode
        else:
            self.rear.next = NewNode
            self.rear = NewNode
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            self.rear = None
            return
        else:
            curr = self.front
            print("Deleted Node: ",curr.data)
            self.front = curr.next
    def printqueue(self):
        curr = self.front
        while curr:
            print(curr.data,end=" ")
            curr = curr.next
        print()

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.printqueue()

queue.dequeue()
queue.dequeue()
queue.printqueue()