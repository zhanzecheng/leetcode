# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午4:15
# @Author  : zhanzecheng
# @File    : 41. 找乱序数组最小数.py
# @Software: PyCharm
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        nums.append(0)
        length = len(nums)
        for i in range(length):
            if nums[i] < 1 or nums[i] >= length:
                nums[i] = 0
        for i in range(length):
            nums[nums[i] % length] += length
        for i in range(length)[1:]:
            if nums[i] // length == 0:
                return i

        return length