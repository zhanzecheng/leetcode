# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午1:54
# @Author  : zhanzecheng
# @File    : 123.卖股票的最好时机.py
# @Software: PyCharm
"""


# 核心思路还是DP，找递推公式

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        k = 3
        result = -11
        dp = [ [0] * len(prices) for x in range(k)]
        for k in range(1, 3):
            tmpMax = dp[k-1][0] - prices[0]
            for i in range(1, len(prices)):
                dp[k][i] = max(dp[k][i-1], prices[i] + tmpMax)
                tmpMax = max(tmpMax, dp[k-1][i] - prices[i])
                result = max(result, dp[k][i])
        return result

if __name__ == '__main__':
    solution = Solution()
    data =[7,1,5,3,6,4]
    print(solution.maxProfit(data))