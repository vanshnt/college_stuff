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
    
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while temp and p < pos - 1:
                temp = temp.next
                p+=1
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
                temp.next = new_node
        
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
list1.insert(Node(60), 3)
list1.printt()