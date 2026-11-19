class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class Hospital:
    def __init__(self):
        self.front = None

    # add patient
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # print next patient
    def display_next(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Next Patient:", self.front.name)

    # delete patient
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next

    # print all patients
    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return

        temp = self.front

        while temp != None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next

patient = Hospital()

patient.enqueue(Node(101, "Atharv", 3))
patient.enqueue(Node(102, "Sonal", 4))
patient.enqueue(Node(103, "Tanaya", 2))
patient.enqueue(Node(104, "Sanjana", 1))

print("All Waiting Patients:")
patient.display_all()

print("\nNext Patient:")
patient.display_next()

print("\nAfter Treatment:")
patient.dequeue()

print("\nRemaining Patients:")
patient.display_all()

print("\nNext Patient:")
patient.display_next()

print("\nAfter Treatment:")
patient.dequeue()

print("\nRemaining Patients:")
patient.display_all()