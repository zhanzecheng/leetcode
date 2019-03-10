# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/7 下午6:38
# @Author  : zhanzecheng
# @File    : 198.房子劫匪.py
# @Software: PyCharm
"""

# TODO: check 1 max(dp[i-2], dp[i-3)

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        if length == 3:
            return max(nums[1], nums[2] + nums[0])
        dp = [0] * length
        # 初始化dp
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        max_cur = max(dp[0], dp[1], dp[2])
        for i in range(3, length):
            dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i]
            max_cur = max(dp[i], max_cur)
        return max_cur
