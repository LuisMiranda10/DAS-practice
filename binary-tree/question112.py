# Link: https://leetcode.com/problems/path-sum/description/
# Path Sum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root is None:
            return False

        if not root.left and not root.right and targetSum == root.val:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        