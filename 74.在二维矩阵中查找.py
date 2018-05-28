# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 上午10:04
# @Author  : zhanzecheng
# @File    : 74.在二维矩阵中查找.py
# @Software: PyCharm
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        实质上是二插查找
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m, n = len(matrix), len(matrix[0])

        left = 0 * n + 0
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2
            m_m = mid // n
            m_l = mid % n
            if matrix[m_m][m_l] < target:

                left = mid + 1
            elif matrix[m_m][m_l] > target:
                right = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
     matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
     solution = Solution()
     print(solution.searchMatrix(matrix, 4))