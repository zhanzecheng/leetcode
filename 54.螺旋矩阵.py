# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午10:07
# @Author  : zhanzecheng
# @File    : 54.螺旋矩阵.py
# @Software: PyCharm
"""

class Solution:
    def __init__(self):
        self.result = []
    def spiralOrder(self, matrix):
        self._spiralOrder(matrix)
        return self.result
    def _spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        if len(matrix) == 1:
            for i in matrix[0]:
                self.result.append(i)
            return
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                self.result.append(matrix[i])
            return
        for i in matrix[0]:
            self.result.append(i)


        for i in range(1, len(matrix)):
            self.result.append(matrix[i][-1])

        for i in range(len(matrix[-1])-2, -1, -1):
            self.result.append(matrix[-1][i])

        for i in range(len(matrix) - 2, 0, -1):
            self.result.append(matrix[i][0])

        for i in range(len(matrix)):
            matrix[i] = matrix[i][1:-1]
        self.spiralOrder(matrix[1:-1])

if __name__ == '__main__':

    solution = Solution()
    data =[[3],[2]]

    print(solution.spiralOrder(data))



