# Meduim
# https://leetcode.com/problems/path-sum-ii/

'''
Runtime: 74 ms, faster than 52.99% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 72.84% of Python3 online submissions for Path Sum II.
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        self.dfs(root, [], answer, targetSum)
        return answer
    

    def dfs(self, root: Optional[TreeNode], path: List[int], answer: List[int], curSum: int) -> None:
        if root is None: return
        
        path.append(root.val) 
        if root.left is None and root.right is None and curSum == root.val:
            answer.append(list(path))
            
        self.dfs(root.left, path, answer, curSum - root.val)
        self.dfs(root.right, path, answer, curSum - root.val)
        path.pop() # backtrack
