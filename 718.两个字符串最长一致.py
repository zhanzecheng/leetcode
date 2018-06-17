# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午1:59
# @Author  : zhanzecheng
# @File    : 718.两个字符串最长一致.py
# @Software: PyCharm
"""

# 核心思路还是使用了DP的算法来找

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0] * len(B) for _ in range(len(A))]

        for i in range(len(A)):
            if A[i] == B[0]:
                dp[i][0] = 1

        for i in range(len(B)):
            if B[i] == A[0]:
                dp[0][i] = 1
        max_v = 0
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                max_v = max(max_v, dp[i][j])
        return max_v