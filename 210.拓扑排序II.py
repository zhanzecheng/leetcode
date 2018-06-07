# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 下午12:35
# @Author  : zhanzecheng
# @File    : 210.拓扑排序II.py
# @Software: PyCharm
"""
from queue import Queue
class Solution:
    def findOrder(self, numCourses, prerequisites):
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
        res = []
        quene = Queue()
        for i in range(len(degree)):
            if degree[i] == 0:
                quene.put(i)
        while not quene.empty():
            cur = quene.get()
            res.append(cur)
            count += 1
            for i in range(numCourses):
                if matrix[cur][i] != 0:
                    matrix[cur][i] = 0
                    degree[i] -= 1
                    if degree[i] == 0:
                        quene.put(i)
        return res
if __name__ == '__main__':
    solution = Solution()
    data = [[1,0]]
    print(solution.findOrder(2, data))