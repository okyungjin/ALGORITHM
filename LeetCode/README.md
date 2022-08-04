# LeetCode
- [Easy](#easy)
  - [190. Reverse Bits](#190-reverse-bits)
  - [268. Missing Number](#268-missing-number)
- [Medium](#medium)
  - [36. Valid Sudoku](#36-valid-sudoku)
- [Hard](#hard)

<br>

## Easy
### [190. Reverse Bits](./190_Reverse_Bits.py)
#### 1차 풀이 (22.08.03)
- bitwise operator를 다루는 문제는 처음이라 낯설었지만 흥미로웠다. 특히 마지막 비트 구하는 `(n >> i) & 1` 로직과 reverse한 bit의 합계를 구하는 `result += 1 << (31 - i)` 로직이 인상깊었다.

```py
class Solution:
    def reverseBits(self, n: int) -> int:
        MAX_SIZE = 32
        result = 0

        for i in range(MAX_SIZE):
            last_bit = (n >> i) & 1
            if last_bit:
                result += 1 << (31 - i)

        return result
```

### [268. Missing Number](./268_Missing_Number.py)
#### 1차 풀이 (22.08.02)
- 문제 요구사항인 time complexiy `O(n)` 은 만족하지만, `num_dict` 때문에 space complexity인 `O(1)` 은 만족하지 못한다. (`num_dict` 의 space complexity는 `O(n)`)
- **문제를 꼼꼼하게 읽고 complexity를 고려하면서 로직을 작성하도록 하자.**

```py
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = dict.fromkeys(nums)
        
        for i in range(len(nums)):
            if not i in num_dict: return i

        return i + 1
```

 
<br>

## Medium
### [36. Valid Sudoku](./36_Valid_Sudoku.py)
#### 1차 풀이 (22.08.02)
- 일단 풀어보자는 마인드로 접근한 시도는 좋았다.
- 시도는 좋았으나 for문을 row, col, sub-box 마다 반복했다는 점에서 이 풀이는 성능이 떨어진다.
- `sub_box_start_points` 에 상수로 sub-box의 시작점을 정해주었는데, board size가 조금만 커질 경우에는 적용이 어려워진다. 상수로 문제를 간단하게 만든 것은 좋은 접근이지만 저 시작점들을 수식으로 표현해보자.

```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check validation by row
        for row in board:
            dic = {}
            for elem in row:
                if elem == '.': continue
                if elem in dic: return False
                else: dic[elem] = 1
        
        # check validation by column
        for i in range(BOARD_SIZE):
            dic = {}
            for j in range(BOARD_SIZE):
                elem = board[j][i]
                if elem == '.': continue
                if elem in dic: return False
                else: dic[elem] = 1

        # check validation by sub-box
        sub_box_start_points = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for (i, j) in sub_box_start_points:
            dic = {}
            range_i = [i for i in range(i, i + 3)]
            range_j = [j for j in range(j, j + 3)]
            
            for x in range_i:
                for y in range_j:
                    elem = board[x][y]
                    if elem == '.': continue
                    if elem in dic: return False
                    else: dic[elem] = 1
        return True
```

<br>


## Hard