# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 上午9:43
# @Author  : zhanzecheng
# @File    : 63. 不同路径-有障碍.py
# @Software: PyCharm
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1] * n for _ in range(m)]

        flag = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                flag = True
                dp[i][0] = 0
            if flag:
                dp[i][0] = 0
        if n == 1 and flag:
            return 0
        flag = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                flag = True
                dp[0][i] = 0
            if flag:
                dp[0][i] = 0
        if m == 1 and flag:
            return 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j] == 1:
                    dp[i - 1][j] = 0
                if obstacleGrid[i][j-1] == 1:
                    dp[i][j-1] = 0
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
if __name__ == '__main__':
    solution = Solution()
    data = [
        [0,0],
        [1,1],
        [0,0]]
    print(solution.uniquePathsWithObstacles(data))