from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        return []


solution = Solution()

''' TestCase #1
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
'''
print(solution.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 'abaedcd'))
