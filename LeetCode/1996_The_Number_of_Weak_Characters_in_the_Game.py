from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x: (-x[0], x[1]))        
        result = max_defense =  0
        
        for _, defense  in properties:
            if defense < max_defense:
                result +=  1
            else:
                max_defense = defense
        return result
        

solution = Solution()
print(solution.numberOfWeakCharacters([[5,5],[6,3],[3,6]])) # 0
print(solution.numberOfWeakCharacters([[2,2],[3,3]])) # 1
print(solution.numberOfWeakCharacters([[1,5],[10,4],[4,3]])) # 1
