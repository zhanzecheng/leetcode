# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/26 下午6:52
# @Author  : zhanzecheng
# @File    : 576.找出界的次数.py
# @Software: PyCharm
"""

# 可以用dp也可以用dfs
# dp[k][i][j] 表示移动k次， i，j区域的次数，则dp[k][i][j]为附近的和，bound的时候为2

# 下面这个是用dfs的
class Solution:
    def __init__(self):
        self.dic = {}

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        if N >= 0 and (i < 0 or j < 0 or i >= m or j >= n):
            return 1
        if N < 0:
            return 0
        if (i, j, N) not in self.dic:
            for p in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if (i, j, N) not in self.dic:
                    self.dic[(i, j, N)] = self.findPaths(m, n, N - 1, i + p[0], j + p[1])
                else:
                    self.dic[(i, j, N)] += self.findPaths(m, n, N - 1, i + p[0], j + p[1])
        return self.dic[(i, j, N)] % (10 ** 9 + 7)