from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ', ' + str(self.next)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # flat list node
        num1 = self.extractValsOfListNodes(l1)
        num2 = self.extractValsOfListNodes(l2)

        print(num1, num2)
             

        return ListNode(1)


    def extractValsOfListNodes(self, node: Optional[ListNode]):
        cur_node = node
        vals = []
        while True:
            if not cur_node or not cur_node.val: return vals
            vals.append(cur_node.val)
            cur_node = cur_node.next


        



    

    
solution = Solution()
# print(solution.addTwoNumbers([2,4,3], [5,6,4])) # [7,0,8] / Explanation: 342 + 465 = 807

print(solution.addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4)))
)) # [7,0,8] / Explanation: 342 + 465 = 807

# print(solution.addTwoNumbers([0], [0])) # [0]
# print(solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])) # [8,9,9,9,0,0,0,1]
