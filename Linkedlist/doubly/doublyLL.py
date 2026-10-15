class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append (self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node
    def printt(self):
        current = self.head
        print("List elements: ")
        while current:
            print(current.data)
            current = current.next
            
list1 = LinkedList()
list1.append(Node(1))
list1.append(Node(2))
list1.append(Node(3))
list1.append(Node(4))

list1.printt()