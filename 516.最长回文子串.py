# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/18 下午4:12
# @Author  : zhanzecheng
# @File    : 516.最长回文子串.py
# @Software: PyCharm
"""


# 这题也是真够难的。。。
# 用间隔序列来处理，牛

# 这一题需要注意一下处理的顺序
# TODO: check 1
class Solution:
    # 当一维想不通时，我们可以使用一下二维的dp来处理
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        print(dp)
        return dp[0][len(s) - 1]
if __name__ == '__main__':
    solution = Solution()
    data = 'bbbab'
    solution.longestPalindromeSubseq(data)