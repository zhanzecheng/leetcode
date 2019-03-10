# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/10 下午2:08
# @Author  : zhanzecheng
# @File    : 238.除了自己的乘积.py
# @Software: PyCharm
"""

# 这道题的trick才是真的重
# 建议多看几遍

# TODO: check 1
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = []
        p = 1
        for i in range(length):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(length-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output