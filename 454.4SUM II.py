# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 下午6:48
# @Author  : zhanzecheng
# @File    : 454.4SUM II.py
# @Software: PyCharm
"""
# 这一题其实是一种hash表的思路

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        dic = {}
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a + b] += 1
                else:
                    dic[a + b] = 1
        re = 0
        for c in C:
            for d in D:
                if -(c + d) in dic:
                    re += dic[-(c + d)]

        return re

