

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_root = 0
    
    def sumNumbers(self, root):
        if root is None: return 0
        return self.sumNumbers_recursive(root)
    
    #def sumNumbers_recursive(self, root):
        #nao terminei ainda