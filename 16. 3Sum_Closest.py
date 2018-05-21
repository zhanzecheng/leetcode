# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/19 上午10:00
# @Author  : zhanzecheng
# @File    : 16. 3Sum_Closest.py
# @Software: PyCharm
"""

'''
和上一题很类似
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        closest = 11111111
        for i in range(length - 2):
            r = length - 1
            l = i + 1
            closest_tmp = 1111111
            while l < r:
                tmp = nums[i] + nums[r] + nums[l]
                if tmp < target:
                    l += 1
                else:
                    r -= 1
                if abs(tmp - target) < abs(closest_tmp - target):
                    closest_tmp = tmp
            if abs(closest - target) > abs(closest_tmp - target):
                closest = closest_tmp
        return closest