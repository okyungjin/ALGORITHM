# Meduim
# https://leetcode.com/problems/design-circular-queue/

from collections import deque

'''
Runtime: 137 ms, faster than 30.13% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.6 MB, less than 21.40% of Python3 online submissions for Design Circular Queue.
'''
class MyCircularQueue:
    def __init__(self, k: int):
        self.__k = k
        self.__queue = deque([])
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.__queue.append(value)
        return True
            
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.__queue.popleft()
        return True

    def Front(self) -> int:
        return self.__queue[0] if not self.isEmpty() else -1


    def Rear(self) -> int:
        return self.__queue[-1] if not self.isEmpty() else -1
    

    def isEmpty(self) -> bool:
        return len(self.__queue) == 0
        
    def isFull(self) -> bool:
        return len(self.__queue) >= self.__k
