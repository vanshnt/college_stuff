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
    def delete(self, data):
        curr = self.head

        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev

                return

            curr = curr.next
                
        
    def printt(self):
        current = self.head
        print("List elements: ")
        while current:
            print(current.data, end = " ")
            current = current.next
            
    def occurance(self, data):
        curr = self.head
        count = 0
        while curr != None:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count
    
    def swap(self):
        if self.head == None or self.head.next == None:
            return

        first = self.head
        last = self.head

        while last.next:
            last = last.next

        second = first.next
        second_last = last.prev

        if first.next == last:
            first.next = None
            first.prev = last
            last.next = first
            last.prev = None
            self.head = last
        else:
            last.prev = None
            last.next = second
            second.prev = last

            second_last.next = first
            first.prev = second_last
            first.next = None

            self.head = last
            
list1 = LinkedList()
list1.append(Node(1))
list1.append(Node(2))
list1.append(Node(3))
list1.append(Node(4))
list1.printt()
list1.insert(Node(60), 3)
list1.printt()
print("\n___ deletion")
list1.delete(3)
list1.printt()
print("\n__ occurance")
print(list1.occurance(2))

print("\n ___Swap")
list1.swap();
list1.printt()

