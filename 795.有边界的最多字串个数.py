# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 下午3:57
# @Author  : zhanzecheng
# @File    : 795.有边界的最多字串个数.py
# @Software: PyCharm
"""


class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        if not A:
            return 0

        dp = [0] * len(A)
        count = 0
        flag = False
        if A[0] >= L and A[0] <= R:
            dp[0] = 1
        elif A[0] <= R:
            count = 1
            flag = True

        for i in range(1, len(A)):
            if A[i] > R:
                flag = False
                count = 0
                continue
            if A[i] >= L and A[i] <= R:
                dp[i] = dp[i - 1] + 1
                if flag:
                    flag = False
                    dp[i] += count
                    count = 0
            else:
                flag = True
                count += 1
                dp[i] = dp[i - 1]
        return sum(dp)