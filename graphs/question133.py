# Link: https://leetcode.com/problems/clone-graph/description/
# Clone Graph

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        
        queue = deque([node])
        cloned_hasher = {}
        cloned_hasher[node.val] = Node(node.val, [])
        
        while queue:
            curr = queue.popleft()
            curr_hasher = cloned_hasher[curr.val] 
            
            for n in curr.neighbors:
                if n.val not in cloned_hasher:
                    queue.append(n)        
                    cloned_hasher[n.val] = Node(n.val, [])
                
                curr_hasher.neighbors.append(cloned_hasher[n.val])
        
        return cloned_hasher[node.val]