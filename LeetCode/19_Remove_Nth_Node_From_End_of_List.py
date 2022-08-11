# Meduim
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        left = dummy
        right = dummy

        for i in range(n):
            right = right.next

        while right.next != None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


solution = Solution()

list_nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(solution.removeNthFromEnd(list_nodes, 2))