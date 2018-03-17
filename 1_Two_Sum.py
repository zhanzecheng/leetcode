# -*- coding: utf-8 -*-
"""
# @Time    : 2017/9/21 下午1:40
# @Author  : zhanzecheng
# @File    : 1_Two_Sum.py
# @Software: PyCharm
"""

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

a = [1,2]
b = a
b[0] = 10
print a

# here is my solution
# O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return list((i, j))
        return []

# here is the good solution
class FinalSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        length = len(nums)
        dic = dict()
        for i in range(length):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i

