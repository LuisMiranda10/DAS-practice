# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# Design Add and Search Words Data Structure

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.isEndOfWord = True; 
    
    def search(self, word):
        return self.search_helper(word, 0)

    def search_helper(self, word, index):
        curr = self
        for i in range(index, len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children.values():
                    if ch.search_helper(word, i+1): 
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.isEndOfWord

    
tree = WordDictionary()
tree.addWord("bad")
tree.addWord("dad")
tree.addWord("mad")

print(tree.search(".ad"))
print(tree.search("b.."))
print(tree.search("pad"))  # False