# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/15 下午9:45
# @Author  : zhanzecheng
# @File    : 152.最大连续乘积序列.py
# @Software: PyCharm
"""
# 超级漂亮。。。。。

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        re = nums[0]

        reM = reN = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                reM, reN = reN, reM

            reM = max(reM * nums[i], nums[i])
            reN = min(reN * nums[i], nums[i])

            re = max(re, reM)
        return re