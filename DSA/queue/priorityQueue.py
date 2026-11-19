class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return
            
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return
        else:
            temp = self.front
            while temp.next:
                if new_node.priority <= temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next
            prev.next = new_node
            new_node.next = temp
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

pq = Queue()
pq.enqueue(node(10,2))
pq.enqueue(node(20,1))
pq.enqueue(node(30,3))
pq.enqueue(node(40,4))
pq.display()