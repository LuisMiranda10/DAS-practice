# Link: https://leetcode.com/problems/recover-binary-search-tree/description/
# Recover Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr_root = root.val
        return self.recoverTree_recursive(self, root)    
    
    def recoverTree_recursive(self, root):
        if not root: return None
        
        
                
        
        