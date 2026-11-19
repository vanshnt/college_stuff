class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        if self.top == None:
            return self.top is None
    def push(self, data):
        newnode = Node(data)
        if self.isempty():
            self.top = newnode
            newnode = self.top
        else:
            newnode.next = self.top
            self.top = newnode
            
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        temp = self.top
        self.top = self.top.next
        temp = None
        
    def print(self):
        curr = self.top
        while curr:
            print(curr.data, end = " ")
            curr = curr.next
        print()
        
    def reverse(self):
        curr = self.top
        while curr:
            newstack.push(curr.data)
            curr = curr.next

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.print()

s.pop()
s.print()
        
newstack = stack()
s.reverse()
newstack.print()