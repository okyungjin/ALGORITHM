from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' Recursion
Runtime: 52 ms, faster than 38.35% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.7 MB, less than 96.73% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


solution = Solution()

''' TestCase #1
Input: root = [1,null,2,3]
Output: [1,3,2]
'''
print(solution.inorderTraversal(
    TreeNode(
        1,
        None,
        TreeNode(
            2,
            TreeNode(3)))))

''' TestCase #2
Input: root = []
Output: []
'''
print(solution.inorderTraversal(None))

''' TestCase #3
Input: root = [1]
Output: [1]
'''
print(solution.inorderTraversal(TreeNode(1)))