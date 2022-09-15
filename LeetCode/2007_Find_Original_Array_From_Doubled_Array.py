# Meduim
# https://leetcode.com/problems/find-original-array-from-doubled-array/

'''
Runtime: 3106 ms, faster than 17.58% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 31.9 MB, less than 79.36% of Python3 online submissions for Find Original Array From Doubled Array.
'''
class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2: return []

        counter, answer = Counter(changed), []
        for x in sorted(counter.keys()):
            if counter[x] > counter[x * 2]: return []
            if x == 0:
                if counter[x] % 2: return []
                else: answer += [0] * (counter[x] // 2)
            else:
                answer += [x] * counter[x]
            counter[2 * x] -= counter[x]

        return answer
