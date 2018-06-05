# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午7:05
# @Author  : zhanzecheng
# @File    : 59.旋转矩阵II.py
# @Software: PyCharm
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0] * n for _ in range(n)]

        if n == 0:
            return []

        num = 1
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                matrix[row_start][i] = num
                num += 1
            row_start += 1
            for i in range(row_start, row_end + 1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1
            for i in range(col_end, col_start - 1, -1):
                matrix[row_end][i] = num
                num += 1
            row_end -= 1
            for i in range(row_end, row_start-1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1
        return matrix


