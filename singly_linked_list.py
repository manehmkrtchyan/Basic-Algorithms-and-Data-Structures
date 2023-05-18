class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str((self.value, f"next id: {id(self.next)}"))
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push_front(self, value):
        new_head = Node(value)
        if len(self) != 0:
            self.head, new_head.next = new_head, self.head
        else: self.head = new_head

    def insert(self, value, pos):
        if pos > len(self) + 1 or pos < 0:
            raise IndexError
        else:
            current = self.head
            for i in range(1, pos):
                current = current.next
            tmp = current.next
            current.next = (new := Node(value))   
            new.next = tmp

    def push_back(self, value):
        node = Node(value)      
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def find(self, value):
        for idx, val in enumerate(self):
            if val.value == value:
                return idx 

    def delete(self, pos):
        current = self.head 
        for i in range(1, pos):
            current = current.next 
        new_next = current.next.next
        to_be_deleted = current.next
        del to_be_deleted
        current.next = new_next

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
        return str([node.value for node in self])
