# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Construct Binary Tree from Preorder and Inorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        index_inorder = inorder.index(root)
        
        root.left = self.buildTree(inorder[:index_inorder])
        root.right = self.buildTree(inorder[index_inorder+1:])
        
        return root