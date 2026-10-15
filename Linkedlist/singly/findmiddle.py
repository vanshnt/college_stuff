class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def middle(self):
        node1 = node2 = self.head

        while node1 and node1.next:
            node2 = node2.next
            node1 = node1.next.next

        print(node2.data)
    
    def printt(self, head):
        current = head
        while current:
            print(current.data, end=" ") 
            current = current.next
            
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

head = a
a.next = b
b.next = c
c.next = d
d.next = e

list = LinkedList(head)
list.printt(head)
print("")
list.middle()
