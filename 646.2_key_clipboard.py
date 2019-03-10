# -*- coding: utf-8 -*-
"""
# @Time    : 2019/3/10 下午1:53
# @Author  : zhanzecheng
# @File    : 646.2_key_clipboard.py
# @Software: PyCharm
"""
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            if i == 0:
                continue
            if i == 1:
                dp[i] = 0
                continue
            # if i % 2 == 0:
            #     dp[i] = dp[i//2] + 2
            # else:
            dp[i] = i
            for j in range(1, i // 2):
                if i % j == 0:
                    dp[i] = dp[j] + i // j
        return dp[-1]