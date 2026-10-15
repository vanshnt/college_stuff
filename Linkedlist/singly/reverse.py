#Singly Linear list

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def printt(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode

        self.head = prev


my_list = LinkedList()
my_list.append(Node(10))
my_list.append(Node(20))
my_list.append(Node(30))
my_list.append(Node(40))
my_list.append(Node(55))
my_list.printt()
my_list.reverse()
my_list.printt()