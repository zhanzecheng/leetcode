# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/28 下午12:30
# @Author  : zhanzecheng
# @File    : 240.在二维矩阵中查找II.py
# @Software: PyCharm
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        m, n = len(matrix), len(matrix[0])

        cc = 0
        cr = n - 1
        while cc < m and cr >= 0:
            if matrix[cc][cr] == target:
                return True
            elif matrix[cc][cr] < target:
                cc += 1
            else:
                cr -= 1
        return False


if __name__ == '__main__':
    solution = Solution()
    data = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
    print(solution.searchMatrix(data, 28))