class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def delete_first_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
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
list.delete_first_last()
list.printt(list.head)