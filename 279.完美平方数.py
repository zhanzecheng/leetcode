# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/15 上午10:02
# @Author  : zhanzecheng
# @File    : 279.完美平方数.py
# @Software: PyCharm
"""
import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [1000000] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            tmp = 10000
            while j * j <= i:
                tmp = min(tmp, dp[i - j* j] + 1)
                j += 1
            dp[i] = tmp
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(12))