# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/25 上午9:33
# @Author  : zhanzecheng
# @File    : 659.分割为连续递增序列.py
# @Software: PyCharm
"""
# 这一题是使用了优先队列和 map的做法 还使用了贪心的策略
import heapq
class Solution(object):
    def isPossible(self, A):
        runs = {} # end -> [lengths]
        for v in A:
            if v - 1 not in runs:
                if v not in runs:
                    runs[v] = [1]
                else:
                    heapq.heappush(runs[v], 1)
            else:
                length = heapq.heappop(runs[v-1]) + 1
                if len(runs[v-1]) == 0:
                    del runs[v-1]
                if v not in runs:
                    runs[v] = []
                heapq.heappush(runs[v], length)
        for v, arr in runs.items():
            if len(arr) > 0 and min(arr) < 3:
                return False
        return True