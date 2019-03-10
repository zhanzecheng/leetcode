# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 上午11:04
# @Author  : zhanzecheng
# @File    : 207.拓扑排序.py
# @Software: PyCharm
"""

# 这一题是使用了拓扑排序来完成的

# 并且通过matrix建立了邻接矩阵
# 通过python内置的quene来建立队列，包括 get put qsize方法

from queue import Queue
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # 这一步是建立一个邻接矩阵
        matrix = [[0] * numCourses for _ in range(numCourses)]
        degree = [0] * numCourses
        for de in prerequisites:
            ready = de[0]
            pre = de[1]
            if matrix[pre][ready] == 0:
                degree[ready] += 1
                matrix[pre][ready] = 1

        count = 0
        quene = Queue()
        for i in range(len(degree)):
            if degree[i] == 0:
                quene.put(i)
        while not quene.empty():
            cur = quene.get()
            count += 1
            for i in range(numCourses):
                if matrix[cur][i] != 0:
                    matrix[cur][i] = 0
                    degree[i] -= 1
                    if degree[i] == 0:
                        quene.put(i)
        return count == numCourses
if __name__ == '__main__':
    solution = Solution()
    data = [[1,0]]
    print(solution.canFinish(2, data))