# Easy
# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Runtime: 866 ms, faster than 89.06% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.7 MB, less than 46.21% of Python3 online submissions for Palindrome Linked List.
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        reversedVals = vals[::-1]

        return vals == reversedVals
        

solution = Solution()
print(solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))) # True
print(solution.isPalindrome(ListNode(1, ListNode(2)))) # False
'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false  
'''