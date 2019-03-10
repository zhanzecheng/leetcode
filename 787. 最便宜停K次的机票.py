# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/21 下午3:46
# @Author  : zhanzecheng
# @File    : 787. 最便宜停K次的机票.py
# @Software: PyCharm
"""

# 这一题使用了神奇的优先队列来做，很是厉害

import heapq

# 直接来比较k次
# 一道优先队列的好题
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        path = [[-1] * n for _ in range(n)]
        for a, b, c in flights:
            path[a][b] = c

        heap = [(0, src, K + 1)]
        while heap:
            tmpc, tmps, tmpk = heapq.heappop(heap)
            # 这里的终止判断也很重要
            if tmps == dst:
                return tmpc
            if tmpk > 0:
                for i in range(n):
                    if path[tmps][i] != -1:
                        heapq.heappush(heap, (path[tmps][i] + tmpc, i, tmpk - 1))
        return -1