# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Runtime: 32 ms, faster than 97.45% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.3 MB, less than 51.52% of Python3 online submissions for Binary Tree Level Order Traversal.
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        answer = []
        
        nodeValByLevel = []
        prevLevel = 0
        
        while queue:
            node, curLevel = queue.popleft()
            
            if prevLevel != curLevel:
                answer.append(nodeValByLevel)
                nodeValByLevel = []
                prevLevel = curLevel
            
            nodeValByLevel.append(node.val)
            if node.left: queue.append((node.left, curLevel + 1))
            if node.right: queue.append((node.right, curLevel + 1))
        
        if nodeValByLevel:
            answer.append(nodeValByLevel)
        
        return answer
            

solution = Solution()

''' TestCase #1
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''
print(solution.levelOrder(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)))))
