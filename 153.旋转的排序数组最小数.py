# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 上午10:31
# @Author  : zhanzecheng
# @File    : 153.旋转的排序数组最小数.py
# @Software: PyCharm
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]