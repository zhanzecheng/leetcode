# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午2:03
# @Author  : zhanzecheng
# @File    : 120.三角形的最少和.py
# @Software: PyCharm
"""

# TODO: check 1
# 又是一道动态规划的题目

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        dp = [[1000] * col for _ in range(row)]
        dp[0][0] = triangle[0][0]
        for r in range(1, row):
            for c in range(len(triangle[r])):
                   if c == 0:
                       dp[r][c] = dp[r-1][c] + triangle[r][c]
                   else:
                       dp[r][c] = min(dp[r-1][c], dp[r-1][c-1]) + triangle[r][c]
        return min(dp[-1])
if __name__ == '__main__':
    solution = Solution()
    data =[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(solution.minimumTotal(data))