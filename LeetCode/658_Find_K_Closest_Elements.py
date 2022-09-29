# Meduim
# https://leetcode.com/problems/find-k-closest-elements/

'''
Runtime: 837 ms, faster than 13.05% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.5 MB, less than 80.93% of Python3 online submissions for Find K Closest Elements.
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sortedByclosest = sorted(arr, key=lambda n: abs(n - x))
        return sorted(sortedByclosest[:k])