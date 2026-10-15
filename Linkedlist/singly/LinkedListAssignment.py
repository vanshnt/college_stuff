class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, position, value):
        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(position - 2):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
            
    def printMiddle(self):
        slow = fast = self.head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast= fast.next.next    
        print("\nMiddle: ", slow.data) 
        
    def deleteNode(self, position):
        if position == 1:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(position -2):
                current = current.next
            current.next = current.next.next
    def reverseLinkedList(self):
        previous = None
        current = self.head
        
        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous 
    def sumof2(self):
        current = self.head

        while current != None and current.next != None:
            total = current.data + current.next.data
            print(total, end = " ")
            current = current.next          

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

list = LinkedList(a)
list.insert(2, 15)
list.traverse()
list.printMiddle()
list.deleteNode(4)
list.traverse()
print("")
# list.reverseLinkedList()
# list.traverse()
list.sumof2()