class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_word = True
    
    def prefix_suggestion(self, prefix): # prefixo = ca
        current_node = self.root
        for char in prefix:
            if char not in current_node.children: # se não encontra a letra, quer dizer que ela não está na árvore
                return []
            current_node = current_node.children[char] # percorre a palavra toda, até chegar no ultimo nó, no caso seria o "a"
        
        suggestions = []
        self.find_suggestions(current_node, prefix, suggestions)
        return suggestions
    
    def find_suggestions(self, current_node, prefix, suggestions):
        if current_node.end_of_word:
            suggestions.append(prefix)
            
        for letter, children_node in current_node.children.items(): # passa a letra do filho do current_node, e depois o prefixo atual ("ca", na primeira interação) + a palavra do nó
            self.find_suggestions(children_node,prefix+letter, suggestions)

trie = Trie()
words = ["carro", "casa", "cachorro", "cavalo", "cama", "cupom", "circuito"]
for word in words: trie.insert(word)

# Buscando sugestões para o prefixo 'ca'
print(trie.prefix_suggestion("ca"))
