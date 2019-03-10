# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/26 下午2:46
# @Author  : zhanzecheng
# @File    : 377.CombinationSum 4.py
# @Software: PyCharm
"""


class Solution:
    # 这一题是一个很简单的dp，你应该可以想到的
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0] * (target + 1)

        for i in nums:
            if i < target + 1:
                dp[i] = 1

        for i in range(target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]
        return dp[target]

if __name__ == '__main__':
    solution = Solution()
    data = [1, 2, 4]
    print(solution.combinationSum4(data, 32))