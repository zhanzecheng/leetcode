# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/22 上午10:28
# @Author  : zhanzecheng
# @File    : 139.单词分割.py
# @Software: PyCharm
"""
# 竟然是用dp来解决，真是神奇

# 使用O(n2)的时间复杂度来做
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False

        dp = [False] * len(s)

        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(1, i+1):
                dp[i] = dp[i] or (dp[j-1] and s[j:i+1] in wordDict)
            if dp[i]:
                continue
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    data = 'ab'
    wordDict = ["a","b"]
    print(solution.wordBreak(data, wordDict))