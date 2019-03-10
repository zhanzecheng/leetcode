# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 上午11:32
# @Author  : zhanzecheng
# @File    : 322.硬币问题.py
# @Software: PyCharm
"""

# 一个牛逼的dp算法，好题

# O(amout * coins)
# TODO: check 1
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [90000000] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                dp[i] = min(dp[i], 1 + dp[i-c] if i-c >=0 else 90000000)

        return dp[amount] if dp[amount] != 90000000 else -1
if __name__ == '__main__':
    solution = Solution()
    data = [1, 2, 5]
    amount = 11
    print(solution.coinChange(data, amount))