# Link: https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=trie
# Word Break

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
    
    def search_segmented(self, s, start, memory):
        if start in memory:
            return memory[start]
        
        current_node = self.root
        for i in range(start, len(s)):
            if s[i] not in current_node.children:
                memory[start] = False
                return False
            current_node = current_node.children[s[i]]

            if current_node.end_of_word:
                if i == len(s) - 1 or self.search_segmented(s, i+1, memory):
                    memory[start] = True
                    return True  
        
        memory[start] = False
        return False       
    
lista = ["leet","code"]
trie = Trie()

for word in lista:
    trie.insert(word)
    
s = "leetcode"
memory = {}
print(trie.search_segmented(s, 0, memory))
