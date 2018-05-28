# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 上午9:39
# @Author  : zhanzecheng
# @File    : 62.不同路径.py
# @Software: PyCharm
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':

    solution = Solution()
    m = 7
    n = 3
    print(solution.uniquePaths(m, n))