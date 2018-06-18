# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/17 上午11:24
# @Author  : zhanzecheng
# @File    : 287.查找重复数字.py
# @Software: PyCharm
"""

# 这一题太trick了
# 类似于在链表中找环

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:

            fast = nums[nums[0]]
            slow = nums[0]
            while fast != slow:
                fast = nums[nums[fast]]
                slow = nums[slow]

            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow
        else:
            return -1