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
        n = len(matrix)
        if n == 0:
            return []

        num = 1
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                self.result.append(matrix[row_start][i])
            row_start += 1
            for i in range(row_start, row_end + 1):
                self.result.append(matrix[i][col_end])
            col_end -= 1
            for i in range(col_end, col_start - 1, -1):
                self.result.append(matrix[row_end][i])
            row_end -= 1
            for i in range(row_end, row_start-1, -1):
                self.result.append(matrix[i][col_start])
            col_start += 1
        return self.result

if __name__ == '__main__':

    solution = Solution()
    data =[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

    print(solution.spiralOrder(data))



