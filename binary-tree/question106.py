# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Construct Binary Tree from Inorder and Postorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
    
        # inorder = [9,3,15,20,7]
        # postorder = [9,15,7,20]
    
        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root