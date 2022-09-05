from typing import List
from collections import deque

'''
Runtime: 73 ms, faster than 63.61% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16 MB, less than 50.08% of Python3 online submissions for N-ary Tree Level Order Traversal.
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        nodes = deque([(0, root)])
        vals_by_level = []
        
        while nodes:
            level, node = nodes.popleft()
            if not node.val: continue
            
            if level >= len(vals_by_level):
                vals_by_level.append([val])
            else:
                vals_by_level[level].append(val)

            for child in node.children:
                nodes.append((level + 1, child))

        return vals_by_level
