import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = []
        heapq.heappush(nodes, (0, root))

        level = 1
        node = root
        while nodes:
            if node.left: heapq.heappush(nodes, (level, node.left))
            if node.right: heapq.heappush(nodes, (level, node.right))
            level += 1
            

                


            
            
            



        return averages

    
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
print(solution.averageOfLevels())