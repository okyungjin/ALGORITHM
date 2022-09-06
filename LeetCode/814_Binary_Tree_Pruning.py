# Meduim
# https://leetcode.com/problems/binary-tree-pruning/

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left == None and root.right == None and root.val == 0:
            return None
        
        return root
