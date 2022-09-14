from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' [Memory Limit Exceeded] '''
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        stack = [([], root)]
        paths = []

        while stack:
            vals, node = stack.pop()
            if node is None or node.val == 0: continue

            cur_vals = vals + [node.val]
            if node.left is None and node.right is None:
                paths.append(cur_vals)
                continue
            
            if node.left: stack.append((cur_vals, node.left))
            if node.right: stack.append((cur_vals, node.right))

        palindromicPathCount = 0
        for path in paths:
            palindromicPathCount += self.isPalindromicPath(path)
 
        return palindromicPathCount


    def isPalindromicPath(self, path: List[int]) -> bool:
        counter = [0] * 10
        
        for num in path:
            counter[num] += 1

        # 1) path의 길이가 홀수일 때, counter[num] 값이 홀수인 경우는 only one
        if self.isOdd(len(path)):
            isOddCountExist = False
            for count in counter:
                if self.isOdd(count):
                    if isOddCountExist: return False
                    isOddCountExist = True
            return True

        # 2) path의 길이가 짝수일 때, counter[num] 값은 모두 짝수여야 함
        else:
            for count in counter:
                if self.isOdd(count): return False
            return True


    def isOdd(self, n: int) -> bool:
        return n % 2 != 0


'''
Runtime: 846 ms, faster than 96.26% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 85.8 MB, less than 43.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
'''
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], count = 0) -> int:
        if root is None: return 0

        count ^= 1 << (root.val - 1)

        if root.left is None and root.right is None:
            if count & (count - 1) == 0: return 1
            return 0

        return self.pseudoPalindromicPaths(root.left, count) + self.pseudoPalindromicPaths(root.right, count)


solution = Solution()
print(solution.pseudoPalindromicPaths(
    TreeNode(
        2,
        TreeNode(
            3,
            TreeNode(3),
            TreeNode(1)),
        TreeNode(
            1,
            TreeNode(1))))) # 2

