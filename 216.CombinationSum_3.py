# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/8 上午9:11
# @Author  : zhanzecheng
# @File    : 216.CombinationSum_3.py
# @Software: PyCharm
"""


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        num = [x for x in range(1, 10)]
        self.dfs(num, n, k, [])
        return self.result

    def dfs(self, num, target, n, tmp):

        if sum(tmp) == target and n == 0:
            self.result.append(tmp)
            return
        if n <= 0:
            return
        if sum(tmp) >= target:
            return
        for i in range(len(num)):
            tmp_ = tmp.copy()
            tmp_.append(num[i])
            self.dfs(num[i + 1:], target, n - 1, tmp_)