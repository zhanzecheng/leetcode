# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/22 下午2:36
# @Author  : zhanzecheng
# @File    : 823.乘积二叉树.py
# @Software: PyCharm
"""

# 注意二叉树一般都是一个乘积的关系，想着一题，还有重构二叉树那题，左右子树都是乘积的关系
# 这一题还有一个需要注意的就是是采用dict来做保存

# TODO： check 1

class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 这一步是从微软得到的教训
        if not A:
            return 0

        A.sort()
        dp = {}
        # 这一题是一道很牛逼的DP题
        for i in range(0, len(A)):
            dp[A[i]] = 1
            for j in range(i)[::-1]:
                if A[i] % A[j] == 0 and (A[i] / A[j]) in dp:
                    dp[A[i]] += dp[A[j]] * dp[A[i] / A[j]]
        return sum(list(dp.values())) % (10 ** 9 + 7)