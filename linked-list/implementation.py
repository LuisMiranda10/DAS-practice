class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_front(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        
    def add_to_end(self, value):
        new_node = Node(value)
        if self.tail:
            new_node.previous= self.tail
            self.tail.next = new_node
        else:
            self.head= new_node
        self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        
        removed_value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_value

linked_list = DoublyLinkedList()

linked_list.add_to_front(3)
linked_list.add_to_front(2)
linked_list.add_to_front(1)
linked_list.add_to_end(4)
linked_list.add_to_end(5)

print(linked_list.remove_from_front())
print(linked_list.remove_from_end())
print(linked_list.remove_from_front())
print(linked_list.remove_from_end())