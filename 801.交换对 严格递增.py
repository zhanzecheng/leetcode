# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 上午9:05
# @Author  : zhanzecheng
# @File    : 801.交换对 严格递增.py
# @Software: PyCharm
"""

# 这道题挺难的，dp的方程比较难想到

class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length = len(A)
        if length == 0:
            return 0

        dp1 = [0] * length
        dp2 = [0] * length
        dp1[0] = 1
        for i in range(1, length):
            # 还需要注意一下这里是 if else 的关系
            if A[i] <= A[i - 1] or B[i] <= B[i - 1]:
                # 好奇葩
                # 这个的思路还是很漂亮
                dp1[i] = dp2[i - 1] + 1
                dp2[i] = dp1[i - 1]
            elif A[i] <= B[i - 1] or B[i] <= A[i - 1]:
                dp1[i] = dp1[i - 1] + 1
                dp2[i] = dp2[i - 1]
            else:
                tmp = min(dp1[i - 1], dp2[i - 1])
                dp1[i] = tmp + 1
                dp2[i] = tmp
        # print(dp1, dp2)
        return min(dp1[-1], dp2[-1])