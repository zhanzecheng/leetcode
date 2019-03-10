# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午2:04
# @Author  : zhanzecheng
# @File    : 713.小于K的连续子序列乘积.py
# @Software: PyCharm
"""

# 使用的方式是一个滑动的窗口来统计
# TODO: check 1
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        low = 0
        high = 0
        tmp = 1
        re = 0
        while high < len(nums):
            tmp *= nums[high]
            while low <= high and tmp >= k:
                tmp /= nums[low]
                low += 1
            re = re + (high -low + 1)
            high += 1
        return re