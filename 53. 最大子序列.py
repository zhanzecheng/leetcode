# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午8:01
# @Author  : zhanzecheng
# @File    : 53. 最大子序列.py
# @Software: PyCharm
"""

"""
这是一道动态规划的题
用 [0] * len(nums)
可以快很多
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        for i in range(1, length):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            result = max(result, dp[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    data = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(data))