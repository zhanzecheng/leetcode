# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/19 上午9:23
# @Author  : zhanzecheng
# @File    : 647.有多少个回文子序列.py
# @Software: PyCharm
"""


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [1] * len(s)

        for i in range(1, len(s)):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i] += 1
        return dp[-1]