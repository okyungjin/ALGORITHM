# Easy
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from typing import Optional, List
from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
'''
Runtime: 106 ms, faster than 21.57% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.5 MB, less than 47.94% of Python3 online submissions for Average of Levels in Binary Tree.
'''
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        nodes = deque([(0, root)])
        vals = []

        while nodes:
            level, node = nodes.popleft()
            last_idx = len(vals) - 1

            if level == last_idx:
                vals[last_idx].append(node.val)

            elif level > last_idx:
                vals.append([node.val])

            if node.left: nodes.append((level + 1, node.left))
            if node.right: nodes.append((level + 1, node.right))
            
        averages = [sum(elem) / len(elem) for elem in vals]
        return averages

        

        

        
            

                


            
            
            



        return []

    
solution = Solution()
'''
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
'''
print(solution.averageOfLevels(
    TreeNode(
        3,
        TreeNode(
            9,
            TreeNode(15),
            TreeNode(7)),
        TreeNode(
            20,
            None,
            None))
))


'''
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
'''
# print(solution.averageOfLevels())