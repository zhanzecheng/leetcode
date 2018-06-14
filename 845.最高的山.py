# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/13 下午4:18
# @Author  : zhanzecheng
# @File    : 845.最高的山.py
# @Software: PyCharm
"""

class Solution:
    def longestMountain(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        dp1 = [1] * len(nums)
        for i in range(1, len(nums)):
            dp1[i] = 1
            if nums[i] > nums[i-1]:
                dp1[i] = dp1[j-1] + 1

        dp2 = [1] * len(nums)
        for i in range(1, len(nums))[::-1]:
            if nums[i] < nums[i-1]:
                dp2[i-1] = dp2[i] + 1
        max_len = -1
        for a, b in zip(dp1, dp2):
            max_len = max(a + b - 1, max_len)
        print(dp1, dp2)
        return max_len
if __name__ == '__main__':
    solution = Solution()
    data = [2, 2, 2]
    print(solution.longestMountain(data))