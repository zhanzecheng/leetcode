# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/6 上午10:33
# @Author  : zhanzecheng
# @File    : 154.在重复的排序旋转数组找最小数.py
# @Software: PyCharm
"""

class Solution:
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
            elif nums[mid] == nums[h]:
                h -= 1
            else:
                h = mid
        return nums[l]