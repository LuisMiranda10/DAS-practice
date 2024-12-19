# Link: https://leetcode.com/problems/binary-search-tree-iterator/description/
# Binary Search Tree Iterator

class BSTIterator:
    def __init__(self, root):
        self.stack = []  # Stack para armazenar os nós
        self._push_left(root)

    def _push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        # Pega o nó mais à esquerda
        node = self.stack.pop()
        val = node.val  # Salva o valor do nó
        
        # Se o nó possui um filho à direita, empilha os nós da subárvore direita
        if node.right:
            self._push_left(node.right)
        
        return val

    def hasNext(self):
        # Retorna True se houver elementos na stack
        return len(self.stack) > 0
