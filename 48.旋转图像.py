# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午4:34
# @Author  : zhanzecheng
# @File    : 48.旋转图像.py
# @Software: PyCharm
"""

'''
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''

# 解释的很好，先转置，再逆序
# 确实充满了技巧
# TODO: check1

class Solution:
    """
    这个方法很变态，就是两步：先转置，再逆序
    """
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        length = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length  - 1- j], matrix[i][j]
if __name__ == '__main__':

    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15 ,16]
    ]

    solution = Solution()
    solution.rotate(data)
    print(data)