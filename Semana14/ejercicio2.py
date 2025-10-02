class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise Exception("Deque is empty")
        
        removed_node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        return removed_node.value
    
    def pop_right(self):
        if self.tail is None:
            raise Exception("Deque is empty")
        
        removed_node = self.tail
        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        return removed_node.value
    
    def print_deque(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    


deque = Deque()

deque.push_left(10)
deque.push_right(20)
deque.push_left(5)
deque.push_right(30)

print("Contenido de la deque:")
deque.print_deque()  

left = deque.pop_left()
right = deque.pop_right()

print(f"elemento removido de la izquierda: {left}")   
print(f"elemento removido de la derecha: {right}")   

print("Contenido de la deque después de pop_left y pop_right:")
deque.print_deque()  