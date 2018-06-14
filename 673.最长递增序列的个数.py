# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午2:50
# @Author  : zhanzecheng
# @File    : 673.最长递增序列的个数.py
# @Software: PyCharm
"""
# 能用DP解决的问题就不是问题
# 这道题搞死我
class Solution:
    def findNumberOfLIS(self, nums):

        len_dp = [0] * len(nums)
        num_dp = [0] * len(nums)
        max_len = 0
        max_count = 0
        for i in range(0, len(nums)):
            len_dp[i] = 1
            num_dp[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if len_dp[i] == len_dp[j] + 1:
                        num_dp[i] += num_dp[j]
                    elif len_dp[i] < len_dp[j] + 1:
                        num_dp[i] = num_dp[j]
                        len_dp[i] = len_dp[j] +1
            if max_len == len_dp[i]:
                max_count += num_dp[i]
            if max_len < len_dp[i]:
                max_len = len_dp[i]
                max_count = num_dp[i]
        return max_count

if __name__ == '__main__':
    solution = Solution()
    data = [1,3,5,4,7]
    print(solution.findNumberOfLIS(data))