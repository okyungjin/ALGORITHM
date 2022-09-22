# Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

''' Recursion
Runtime: 191 ms, faster than 5.36% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 31.69% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int], left = 0, right = 0) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1:]))    
    