class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.pop is None:
            raise Exception("Stack is empty")
        
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()

print("Removed:", stack.pop())

stack.print_stack()