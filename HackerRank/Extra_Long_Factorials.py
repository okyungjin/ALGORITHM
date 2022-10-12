# Meduim
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
    
    print(dp[-1])
    


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
