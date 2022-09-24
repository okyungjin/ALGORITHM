# Easy
# https://leetcode.com/problems/path-sum/

''' DFS
Runtime: 85 ms, faster than 27.42% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 56.22% of Python3 online submissions for Path Sum.
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum)
     
    
    def dfs(self, root, curSum) -> bool:
        if root is None: return False
        
        if root.left is None and root.right is None and curSum == root.val:
            return True
        
        return self.dfs(root.left, curSum - root.val) or self.dfs(root.right, curSum - root.val)
    