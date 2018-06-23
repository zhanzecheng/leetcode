# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/22 上午10:01
# @Author  : zhanzecheng
# @File    : 560.连续子数组的和等于k.py
# @Software: PyCharm
"""


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        dic = {0: 1}

        value = 0
        for i in range(len(nums)):
            value += nums[i]
            if (value - k) in dic:
                count += dic[value - k]
            if value in dic:
                dic[value] += 1
            else:
                dic[value] = 1

        return count