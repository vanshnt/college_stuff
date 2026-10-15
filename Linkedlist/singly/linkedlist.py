class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class LinkedList:
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head

            for i in range(1, pos - 1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node
            return
                
        
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def print(self):
        count = 0
        sum = 0
        temp = self.head
        while (temp):
            count +=1
            sum = sum + temp.data
            print(temp.data)
            temp = temp.next
        print("count", count)    
        print("sum", sum)    

list = LinkedList()
t1 = Node(10)
t2 = Node(20)
t3 = Node(30)

list.append(t1)
list.append(t2)
list.append(t3)
list.append(Node(40))
list.print()


print("-----------")
list.insert(Node(5), 1) 
list.insert(Node(15), 3)
list.insert(Node(25), 5)
list.insert(Node(50), 8)
list.insert(Node(50), 9)


list.print()