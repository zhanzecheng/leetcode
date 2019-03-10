# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 下午7:44
# @Author  : zhanzecheng
# @File    : 64.路径最小和.py
# @Software: PyCharm
"""

# 动态规划
# 这一道题倒是比较简单
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0:
            return 0
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        sum_ = 0
        for i in range(n):
            sum_ += grid[0][i]
            dp[0][i] = sum_
        sum_ = 0
        for i in range(m):
            sum_ += grid[i][0]
            dp[i][0] = sum_

        for i in range(1, m):
            for j in range(1, n):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    data = [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
    print(solution.minPathSum(data))