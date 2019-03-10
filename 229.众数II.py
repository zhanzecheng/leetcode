# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/10 上午10:32
# @Author  : zhanzecheng
# @File    : 229.众数II.py
# @Software: PyCharm
"""

# 这题的trick性依然很强

# 注意初始化的情况

# TODO: check 1
class Solution:

    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]