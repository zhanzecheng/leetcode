# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/11 下午8:06
# @Author  : zhanzecheng
# @File    : 368.最长可以整除的序列.py
# @Software: PyCharm
"""

# 我们这里使用的思路是用一个数组跟踪的存放
# 然后从后往前遍历


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums
        dp = [[] for _ in range(length)]
        # TODO: 这里需不需要一起全局初始化
        dp[0].append(nums[0])
        m_r = 0
        re = []
        for i in range(1, length):
            dp[i] = [nums[i]]
            max_len = 0
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    tmp_len = 0
                    tmp = []
                    for k in dp[j][::-1]:
                        if nums[i] % k == 0:
                            tmp = [k] + tmp
                            tmp_len += 1
                        else:
                            break
                    if tmp_len > max_len:
                        max_len = tmp_len
                        dp[i] = tmp + [nums[i]]
                        if max_len > m_r:
                            m_r = max_len
                            re = dp[i].copy()

        return re

if __name__ == '__main__':
    solution = Solution()
    data = [1, 2, 3, 4, 8]
    print(solution.largestDivisibleSubset(data))