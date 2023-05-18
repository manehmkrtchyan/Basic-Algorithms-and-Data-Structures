class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.value)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def push_front(self, value):
        new = Node(value) 
        new.next = self.head 
        if self.head != None: 
            self.head.prev = new
            self.head = new 
            new.prev = None
        else: 
            self.head = new
            self.tail = new
            new.prev = None 

    def insert(self, value, pos):
        if pos > len(self) + 1 or pos < 0:
            raise IndexError
        else:
            new = Node(value)
            current = self.head
            for i in range(pos):
                current = current.next
            next = current.next
            current.next = new
            new.prev = current
            new.next = next

    def push_back(self, value):
        new = Node(value)
        self.tail.next = new
        new.prev = self.tail
        self.tail = new

    def find(self, value):
        for pos, val in enumerate(self):
            if val.value == value:
                return pos
    
    def delete(self, pos):
        current = self.head 
        for i in range(1, pos):
            current = current.next 
        new_next = current.next.next
        to_be_deleted = current.next
        del to_be_deleted
        current.next = new_next
        new_next.prev = current

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return str([i for i in self])
    
