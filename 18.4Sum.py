# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/19 下午3:46
# @Author  : zhanzecheng
# @File    : 18.4Sum.py
# @Software: PyCharm
"""
'''
这个解析的可是真的很神奇
'''

# 这个使用递归的方式来写很神奇
# TODO：check 1

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = []
        self.find_answer(nums, 4, target, [], results)
        return results

    def find_answer(self, nums, N, target, result, results):
        '''
        '''
        if len(nums) < N or N < 2: return

        length = len(nums)
        if N == 2:
            l = 0
            r = length - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(length - N + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    self.find_answer(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)
