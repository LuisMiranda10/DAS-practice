# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Binary Tree Inorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.output = []
    
    def inorderTraversal(self, root):
        self.inorderTransversal_recursive(root)
        return self.output
    
    def inorderTransversal_recursive(self, root):
        if not root:
            return []
        if root:
            self.inorderTransversal_recursive(root.left)
            self.output.append(root.val)
            self.inorderTransversal_recursive(root.right)
        
        return self.output