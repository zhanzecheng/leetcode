# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/18 上午11:32
# @Author  : zhanzecheng
# @File    : 15.3Sum.py
# @Software: PyCharm
"""

'''
把三个数加起来等于一个特定的数
首先排序
在用首尾指针的方法来找数
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length - 2):
            r = length - 1
            l = i+ 1
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            while l < r :
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r) and nums[l] == nums[l - 1]:
                        l += 1
                elif  nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else  :
                    l += 1
        return result