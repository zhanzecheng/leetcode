# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/3 上午9:14
# @Author  : zhanzecheng
# @File    : 260.找两个只出现一次的数.py
# @Software: PyCharm
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2:
            return []

        diff = nums[0]
        for i in nums[1:]:
            diff ^= i
        diff &= -diff
        d1 = 0
        d2 = 0
        for i in nums:
            if i & diff == 0:
                d1 ^= i
            else:
                d2 ^= i
        return [d1, d2]