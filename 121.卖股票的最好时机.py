# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 上午10:50
# @Author  : zhanzecheng
# @File    : 121.卖股票的最好时机.py
# @Software: PyCharm
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        minPrice = prices[0]
        profit = -1
        for i in prices[1:]:
            profit = max(i - minPrice, profit)
            minPrice = min(i, minPrice)
        if profit > 0:
            return profit
        else:
            return 0