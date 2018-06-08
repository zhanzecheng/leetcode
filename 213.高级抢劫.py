# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/7 下午6:58
# @Author  : zhanzecheng
# @File    : 213.高级抢劫.py
# @Software: PyCharm
"""
# 核心思路就是使用了两次dp来解决
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
            return max(nums[1], nums[2] , nums[0])
        dp = [0] * length
        # 初始化dp
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        path = [0] * length
        path[0] = 1
        path[2] = 1
        max_cur = max(dp[0], dp[1], dp[2])
        for i in range(3, length-1):
            dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i]
            max_cur = max(dp[i], max_cur)
        t = max_cur

        dp = [0] * (length-1)
        dp[0] = nums[1]
        dp[1] = nums[2]
        dp[2] = nums[1] + nums[3]
        max_cur = max(dp[0], dp[1], dp[2])
        for i in range(3, length-1):
            dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i+1]
            max_cur = max(dp[i], max_cur)

        return max(t, max_cur)
if __name__ == '__main__':
    solution = Solution()
    data = [2, 2, 4, 3, 2, 5]
    print(solution.rob(data))