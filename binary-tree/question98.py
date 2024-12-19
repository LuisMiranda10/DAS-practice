# Link: https://leetcode.com/problems/validate-binary-search-tree/description/
# Validate Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        return self.search_recursive(root, float('-inf'), float('inf'))
    
    def search_recursive(self, root, value_min, value_max):
        if not root:
            return True
        
        if not (value_min < root.val < value_max):
            return False
        
        return self.search_recursive(root.left, value_min, root.val) and self.search_recursive(root.right, root.val, value_max)