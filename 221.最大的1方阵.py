# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/9 上午11:10
# @Author  : zhanzecheng
# @File    : 221.最大的1方阵.py
# @Software: PyCharm
"""


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = 0
        if matrix == []:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                result = 1
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                result = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                if matrix[i][j] == '1' and matrix[i][j] == '0':
                    dp[i][j] = 1
                    continue
                if matrix[i][j] == '1' and matrix[i][j] == '1':
                    length = dp[i - 1][j - 1]
                    l1 = 0
                    l2 = 0
                    for p in range(j - length, j + 1)[::-1]:
                        if matrix[i][p] == '1':
                            l1 += 1
                        else:
                            break
                    for p in range(i - length, i + 1)[::-1]:
                        if matrix[p][j] == '1':
                            l2 += 1
                        else:
                            break
                    min_length = min(l1, l2)
                    dp[i][j] = min_length
                    result = max(result, dp[i][j])
        return result * result