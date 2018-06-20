# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 下午2:02
# @Author  : zhanzecheng
# @File    : 378.排好序数组中第k小的数.py
# @Software: PyCharm
"""

# 我对这一题很无语。。太奇怪了

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]

        while L < R:
            mid = (L + R) >> 1
            temp = sum([self.binary_search(y, mid, n) for y in matrix])
            if temp < k:
                L = mid + 1
            else:
                R = mid
            print(L, R, mid, temp)
        return L

    def binary_search(self, row, x, n):
        L, R = 0, n-1
        while L <= R:
            mid = (L + R) >> 1
            if row[mid] <= x:
                L = mid + 1
            else:
                R = mid - 1
        return L

if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
             ]
    k = 8,
    d = [1, 4, 6, 8, 9, 10, 11, 12]
    print(solution.kthSmallest(matrix, 6))