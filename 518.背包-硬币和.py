# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 上午11:03
# @Author  : zhanzecheng
# @File    : 518.背包-硬币和.py
# @Software: PyCharm
"""

'''
not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
using the ith coin, since we can use unlimited same coin, we need to know how many way to make up amount j - coins[i] by using first i coins(including ith), which is dp[i][j-coins[i]]

'''

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0] * (amount + 1)  for _ in range((len(coins) + 1))]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, len(dp[0])):
                if coins[i-1] > j:
                    tmp = 0
                else:
                    tmp =  dp[i][j-coins[i-1]]
                dp[i][j] = dp[i-1][j] + tmp
        return dp[len(coins)][amount]
if __name__ == '__main__':
    solution = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(solution.change(amount, coins))
