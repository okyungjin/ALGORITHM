# Easy
# https://leetcode.com/problems/construct-string-from-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


''' Recursion
Runtime: 153 ms, faster than 6.19% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.6 MB, less than 10.51% of Python3 online submissions for Construct String from Binary Tree.
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ''

        left_node = f'{self.tree2str(root.left)}'
        right_node = f'{self.tree2str(root.right)}'

        concat = f'{root.val}({left_node})({right_node})'

        return concat.replace('()()', '').replace(')()', ')')



solution = Solution()

''' TestCase #1
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
'''
print(solution.tree2str(
    TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4)),
        TreeNode(3))))

''' TestCase #2
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
'''
print(solution.tree2str(
    TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(4)),
        TreeNode(3))))
