# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 下午2:17
# @Author  : zhanzecheng
# @File    : 96.有多少个不同的二插搜索树.py
# @Software: PyCharm
"""

# 这道题还真的是没有思路
# TODO: 需要多看几遍背下来

# 定义J(i, n)为取顶点i，在序列n上做的唯一的二叉树个数
# 定义G(n)为在序列n上唯一二叉树的总和
# 则 G(n) = J(1, n) + J(2, n) + ... + J(n, n)
# 则 J(i, n) = G(i - 1) * G (n - i)
# 那现在开始写代码
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        # TODO: 这里的初始化 dp[0]=1 一定要注意
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))