# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/25 上午11:46
# @Author  : zhanzecheng
# @File    : 743.dijkstra.py
# @Software: PyCharm
"""

# 使用优先队列可以很好的实现dj算法

import heapq


class Solution:
    def networkDelayTime(self, time, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        path = [[-1] * (N + 1) for _ in range(N + 1)]
        for t in time:
            path[t[0]][t[1]] = t[2]

        fin, res = set(), 0
        queue = []
        heapq.heappush(queue, (0, K))
        while len(queue) and len(fin) != N:
            tmp = heapq.heappop(queue)
            vec = tmp[1]
            fin.add(vec)
            dis = tmp[0]
            res = max(res, dis)
            for t in range(1, N + 1):
                if path[vec][t] != -1:
                    if t in fin: continue
                    heapq.heappush(queue, (dis + path[vec][t], t))

        return res if len(fin) == N else -1