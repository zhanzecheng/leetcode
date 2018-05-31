# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 上午10:51
# @Author  : zhanzecheng
# @File    : 91.解码.py
# @Software: PyCharm
"""


# 这题不是很会

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i-1]
            if s[i-2:i] < '27' and s[i-2:i] > '09':
                dp[i] += dp[i-2]
        return dp[len(s)]

if __name__ == '__main__':
    soluton = Solution()
    data ="1212"
    print(soluton.numDecodings(data))