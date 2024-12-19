# implementação de pilha utilizando um array

class Stack_array:
    def __init__(self, max_lenght=1000):
        self.arr = [0]*max_lenght
        self.max_lenght = max_lenght
        self.pointer = 0
    
    def push(self, item):
        self.arr[self.pointer] = item
        self.pointer += 1
        
    def pop(self):
        if not len(self.arr):
            raise IndexError('Empty List')
        
        return self.arr.pop()
    
    def peek(self): # verifica o valor que está no topo
        if not len(self.arr):
            raise IndexError('Empty List')
        
        return self.arr[-1]
 
    def size(self):
        return self.pointer

# implementação de pilha utilizando uma linked list (metodo tradicional)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_item = Node(item)
        new_item.next = self.top
        self.top = new_item
        self._size += 1
    
    def pop(self):
        if self.top is None: raise IndexError("Empty Stack")
        pop_item = self.top
        self.top = pop_item.next
        self._size -= 1
        return self.top.value
    
    def peek(self):
        if self.top is None: raise IndexError("Empty Stack")
        return self.top.value
    
    def size(self):
        return self._size

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.size())
        