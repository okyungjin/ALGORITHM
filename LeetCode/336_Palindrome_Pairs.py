# Hard
# https://leetcode.com/problems/palindrome-pairs/

'''
Runtime: 8284 ms, faster than 7.39% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 25.8 MB, less than 98.06% of Python3 online submissions for Palindrome Pairs.
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        answer = set()
        for i, word in enumerate(words):
            if not word: continue
            
            for j in range(len(word)):
                cur = word[:j]
                target = word[j:][::-1]
                if cur == cur[::-1] and target != word and target in idx_map:
                    answer.add((idx_map[target], i))
            
            for j in range(len(word), -1, -1):
                cur = word[j:]
                target = word[:j][::-1]
                if cur == cur[::-1] and target != word and target in idx_map:
                    answer.add((i, idx_map[target]))
                    
            if word == word[::-1] and '' in idx_map:
                idx = idx_map['']
                answer.add((i, idx))
                answer.add((idx, i))

        return list(answer)