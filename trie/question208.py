# Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=trie
# Implement Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_word = True
    
    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.end_word
    
    def startsWith(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True