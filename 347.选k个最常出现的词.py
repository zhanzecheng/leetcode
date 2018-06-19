# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/18 上午9:26
# @Author  : zhanzecheng
# @File    : 347.选k个最常出现的词.py
# @Software: PyCharm
"""

from Queue import PriorityQueue


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if nums == []:
            return []

        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        ma = {}
        q = PriorityQueue()
        for key, values in dic.items():
            if values not in ma:
                ma[values] = [key]
                q.put((-values, values))

            else:
                ma[values].append(key)
        re = []
        while len(re) < k:
            tmp = q.get()[1]
            re.extend(ma[tmp])
        return re
