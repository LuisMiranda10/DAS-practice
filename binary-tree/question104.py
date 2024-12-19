# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Maximum Depth of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum_path = float('-inf')
    
    def maxDepth(self, root):
        return self.maxDepth_recursive(root)
    
    def maxDepth_recursive(self, root):
        if not root:
            return 0
            
        if root:
            left_path = self.maxDepth_recursion(root.left)
            right_path = self.maxDepth_recursive(root.right)
            
        self.sum_path = max((1 + left_path + right_path), self.sum_path)
        
        return self.sum_path