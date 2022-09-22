# Easy
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word[::-1] for word in s.split(' ')]
        return ' '.join(words)
