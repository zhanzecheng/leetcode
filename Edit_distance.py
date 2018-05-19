# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/19 下午3:01
# @Author  : zhanzecheng
# @File    : Edit_distance.py
# @Software: PyCharm
"""


def minEditDist(sm, sn):
    '''
    use to check the min_distance
    :param sm:
    :param sn:
    :return:
    '''

    m, n = len(sm) + 1, len(sn) + 1

    # create a matrix(m * n)

    # fast way to create a matrix
    matrix = [[0] * n for i in range(m)]

    # now initial the matrix
    matrix[0][0] = 0

    for i in range(1, m):
        matrix[i][0] = matrix[i-1][0] + 1

    for i in range(1, n):
        matrix[0][i] = matrix[0][i-1] + 1

    for i in range(1, m):
        for j in range(1, n):
            # 这里需要注意下 字符串是从下标0开始的
            cost = 0 if sm[i-1] == sn[j-1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)

    return matrix[m - 1][n - 1]

print(minEditDist('abc', 'adec'))