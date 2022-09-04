# Hard
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

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
Runtime: 66 ms, faster than 20.72% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.1 MB, less than 72.74% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
'''
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_queue = deque([ (root, 0, 0) ])
        heap = []
        answer = []

        while nodes_queue:
            node, row, col = nodes_queue.popleft()

            if node.left: nodes_queue.append((node.left, row + 1, col - 1))
            if node.right: nodes_queue.append((node.right, row + 1, col + 1))

            heapq.heappush(heap, (col, row, node.val))

        prev_col = -987654321
        vals_by_col = []
        while heap:
            col, row, val = heapq.heappop(heap)

            if prev_col == col:
                vals_by_col.append(val)
                
            else:
                if vals_by_col:
                    answer.append(vals_by_col)
                vals_by_col = [val]
                prev_col = col

        if vals_by_col:
            answer.append(vals_by_col)

        return answer



solution = Solution()

print(solution.verticalTraversal(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7))))) # [[9],[3,15],[20],[7]]

print(solution.verticalTraversal(
    TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)),
        TreeNode(
            3,
            TreeNode(6),
            TreeNode(7))))) # [[4],[2],[1,5,6],[3],[7]]

print(solution.verticalTraversal(
    TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(6)),
        TreeNode(
            3,
            TreeNode(5),
            TreeNode(7))))) # [[4],[2],[1,5,6],[3],[7]]

print(solution.verticalTraversal(
    TreeNode(
        3,
        TreeNode(
            1,
            TreeNode(0),
            TreeNode(2)),
        TreeNode(
            4,
            TreeNode(2))))) # [[0],[1],[3,2,2],[4]]