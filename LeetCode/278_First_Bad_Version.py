# Easy
# https://leetcode.com/problems/first-bad-version/

''' Binary Search
Runtime: 57 ms, faster than 20.49% of Python3 online submissions for First Bad Version.
Memory Usage: 13.9 MB, less than 62.20% of Python3 online submissions for First Bad Version.
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n + 1

        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start
