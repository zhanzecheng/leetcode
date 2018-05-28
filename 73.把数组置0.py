# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 上午10:03
# @Author  : zhanzecheng
# @File    : 73.把数组置0.py
# @Software: PyCharm
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -132
                    for low in range(n):
                        if matrix[i][low] != 0:
                            matrix[i][low] = -132
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -132:
                    matrix[i][j] = 0
