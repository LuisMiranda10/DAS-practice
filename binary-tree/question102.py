# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=problem-list-v2&envId=breadth-first-search
# Binary Tree Level Order Traversal

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        queue = deque()
        queue.append(root)
        answer = []
        while(queue):
            aux = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    aux.append(node.val)
                    if node.left:
                        queue.append(node.left)
                
                    if node.right:
                        queue.append(node.right)   
            if aux:
                answer.append(aux)
        return answer
            