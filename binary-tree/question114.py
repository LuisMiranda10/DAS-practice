# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=depth-first-search&difficulty=MEDIUM
# Flatten Binary Tree to Linked List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return None
        
        current = root
        if current.left is not None:
            last = current.left
            while last.right is not None:
                last = last.right

            last.right = current.right
            current.right = current.left
            current.left = None
            
        current = current.right
        