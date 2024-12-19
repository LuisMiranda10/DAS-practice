class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertion_recursive(value, self.root) 
                
    def insertion_recursive(self, value, node):
       if value < node.value:
           if node.left is None:
                node.left = Node(value)
           else:
                self.insertion_recursive(value, node.left)
       else:
           if node.right is None:
                node.right = Node(value)
           else:
                self.insertion_recursive(value, node.right)
    
    def search_recursive(self, value, node):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search_recursive(value, node.left)
        else:
            return self.search_recursive(value, node.right)
    
    def search(self, value):
        return self.search_recursive(value, self.root)
            
            
graph = BinaryTree()
graph.insert(5)
graph.insert(3)
graph.insert(10)
graph.insert(7)
print(graph.search(7))