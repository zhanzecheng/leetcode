# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/18 下午4:09
# @Author  : zhanzecheng
# @File    : 813.最大和的平均划分.py
# @Software: PyCharm
"""


class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """

        dp = [[0] * len(A) for _ in range(K)]
        t = 0
        for i in range(len(A)):
            t += A[i]
            dp[0][i] = t / (i + 1)

        for k in range(1, K):
            for i in range(k, len(A)):
                tmp = 0
                for j in range(i):
                    tmp = max(tmp, dp[k - 1][j] + sum(A[j + 1:i + 1]) / (i - j))
                dp[k][i] = tmp
        return dp[-1][-1]