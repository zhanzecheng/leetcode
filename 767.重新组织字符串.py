# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/21 下午3:18
# @Author  : zhanzecheng
# @File    : 767.重新组织字符串.py
# @Software: PyCharm
"""

# 这一题我们使用优先队列的方法来做
import heapq


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 对字符的频次做一个统计，并有一个先决判断
        dic = {}
        for c in S:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
                if dic[c] > (len(S) + 1) / 2:
                    return ""

        queue = []
        for key, value in dic.items():
            heapq.heappush(queue, [-value, key])
        re = ""
        while len(re) < len(S):
            if len(queue) == 1:
                v1, cur = heapq.heappop(queue)
                re += cur
                break
            v1, cur = heapq.heappop(queue)
            v2, p = heapq.heappop(queue)
            v1 = -v1
            v2 = -v2
            if v1 - 1 >= 0:
                re += cur
                if v1 - 1 > 0:
                    heapq.heappush(queue, [-(v1 - 1), cur])
            if v2 - 1 >= 0:
                re += p
                if v2 - 1 > 0:
                    heapq.heappush(queue, [-(v2 - 1), p])

        return re