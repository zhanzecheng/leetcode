# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午6:45
# @Author  : zhanzecheng
# @File    : 542.01矩阵1.py
# @Software: PyCharm
"""

# 一个简单的循环方式来解决这个问题
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cur = 0
        col = len(matrix[0])
        row = len(matrix)
        while True:
            cur += 1
            flag = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == cur:
                        if i - 1 < 0 or matrix[i - 1][j] >= cur:
                            pass
                        else:
                            continue

                        if j - 1 < 0 or matrix[i][j - 1] >= cur:
                            pass
                        else:
                            continue

                        if i + 1 >= row or matrix[i + 1][j] >= cur:
                            pass
                        else:
                            continue

                        if j + 1 >= col or matrix[i][j + 1] >= cur:
                            pass
                        else:
                            continue
                        flag = True
                        matrix[i][j] += 1
            if not flag:
                break
        return matrix

if __name__ == '__main__':
    solution = Solution()
    data = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(solution.updateMatrix(data))
    data =[
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]
    ]

    result = [
        [1,0,1,1,0,0,1,0,0,1],
        [0,1,1,0,1,0,1,0,1,1],
        [0,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,1],
        [0,1,0,1,1,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,1],
        [1,0,0,0,1,2,1,1,0,1],
        [2,1,1,1,1,1,1,0,1,0],
        [1,2,1,1,0,1,0,0,1,1]
    ]
    true_result = [
        [1,0,1,1,0,0,1,0,0,1],
        [0,1,1,0,1,0,1,0,1,1],
        [0,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,1],
        [0,1,0,1,1,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,1],
        [1,0,0,0,1,2,1,1,0,1],
        [2,1,1,1,1,2,1,0,1,0],
        [3,2,2,1,0,1,0,0,1,1]
    ]
