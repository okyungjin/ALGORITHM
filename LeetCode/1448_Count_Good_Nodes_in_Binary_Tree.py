# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search_node(root, root.val)

    def search_node(self, node: TreeNode, max_num: int) -> int:
        res = 0
        if node.val >= max_num: res += 1
        if node.left: res += self.search_node(node.left, max(max_num, node.val))
        if node.right: res += self.search_node(node.right, max(max_num, node.val))
        return res



solution = Solution()
print(solution.goodNodes(
    TreeNode(3,
        TreeNode(1, TreeNode(3)),
        TreeNode(4, TreeNode(1), TreeNode(5)))
)) # 4