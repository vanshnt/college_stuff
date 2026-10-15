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

    def del_node(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value is not there in the list")

    def printt(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()


my_list = LinkedList()
my_list.append(Node(10))
my_list.append(Node(20))
my_list.append(Node(30))
my_list.append(Node(40))
my_list.append(Node(55))
my_list.del_node(30)
my_list.printt()